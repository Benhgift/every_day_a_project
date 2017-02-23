import zmq
import sqlite3


def insert_into_db(title, year):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO movies VALUES
            ("{}", {})'''.format(title, year)
        )
    conn.commit()
    conn.close()


def get_all_rows():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    rows = list(c.execute('''
        SELECT * FROM movies
        '''))
    conn.close()
    return rows
    

if __name__ == '__main__':
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind('tcp://127.0.0.1:5555')
    while True:
        print("listening for input")
        msg = socket.recv_pyobj()
        if msg == 'get':
            socket.send_pyobj(get_all_rows())
        elif msg.split()[0] == 'put':
            insert_into_db(*msg.split()[1:])
            socket.send_pyobj('inserted row')
