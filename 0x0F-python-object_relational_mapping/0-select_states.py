#!/usr/bin/python3
"""Module to select all states from he database hbtn_0e_0_usa;
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    username, pwd, db_name = argv[1], argv[2], argv[3]

    db = MySQLdb.connect(
            host='localhost',
            user=username,
            password=pwd,
            database=db_name
            )
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY states.id ASC')
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
