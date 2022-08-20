import sqlite3

connection = sqlite3.connect('database.db')

with open('Task-11\schema.sql') as f:
    connection.executescript(f.read())

connection.commit()
connection.close()