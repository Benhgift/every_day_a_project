import zmq
import zlib
import pickle


def connect_client():
    socket = zmq.Context().socket(zmq.REQ)
    socket.connect('tcp://127.0.0.1:5555')
    #socket.connect('tcp://172.17.0.2:5555')
    return socket


if __name__ == '__main__':
    query = input('query: ')
    socket = connect_client()
    socket.send_pyobj(query)
    msg = socket.recv_pyobj()
    print(msg)
