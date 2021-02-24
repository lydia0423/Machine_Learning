#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#Python work well with SQL lite
import sqlite3

def main():
    print('connect')
    #connect to database
    db = sqlite3.connect('db-api.db')
    #cursor: allow the user to keep track where they are in the database when run database commands
    cur = db.cursor()
    print('create')
    #execute SQL
    cur.execute("DROP TABLE IF EXISTS test")
    cur.execute("""
        CREATE TABLE test (
            id INTEGER PRIMARY KEY, string TEXT, number INTEGER
        )
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('one', 1)
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('two', 2)
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('three', 3)
        """)
    print('commit')
    db.commit()
    print('count')
    cur.execute("SELECT COUNT(*) FROM test")
    count = cur.fetchone()[0]
    print(f'there are {count} rows in the table.')
    print('read')
    #to read all rows
    for row in cur.execute("SELECT * FROM test"):
        print(row)
    print('drop')
    cur.execute("DROP TABLE test")
    print('close')
    db.close()

if __name__ == '__main__': main()
