import sqlite3

conn = sqlite3.connect('db_planes.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS planes (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                type_plane TEXT NOT NULL,
                start_date DATE NOT NULL,
                operation_date DATE NOT NULL
            )''')

conn.commit()
conn.close()