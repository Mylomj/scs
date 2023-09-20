import sqlite3


#create database

conn = sqlite3.connect("test_data.db")
c =conn.cursor()

#create table
'''
c.execute(""""CREATE TABLE student(
            first_name text,
            last_name text,
            admno integer,
            course text,
            fee integer,
            fee balance integer
)

""")
'''

conn.commit()

conn.close()
