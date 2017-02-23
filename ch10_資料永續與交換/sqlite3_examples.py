#!encoding:utf8

import sqlite3

conn = sqlite3.connect('db.sqlite3')


c = conn.cursor()
c.execute("""CREATE TABLE if not EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE not NULL,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    msg TEXT NOT NULL
    )  """)

c.execute("INSERT INTO messages VALUES(1,'ihong','ihong@gmail.com','message....') ")

conn.commit()

conn.close()