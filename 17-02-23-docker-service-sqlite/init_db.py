import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

c.execute('''
        CREATE TABLE IF NOT EXISTS movies
            (title text, year int)
        ''')

c.execute('''
        INSERT INTO movies VALUES
        ("matrix", 1999)
        ''')

conn.commit()

conn.close()

