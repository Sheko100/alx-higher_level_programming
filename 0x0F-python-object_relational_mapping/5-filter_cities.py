#!/usr/bin/python3
"""Module to select a state row by name the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    username, pwd, db_name = argv[1], argv[2], argv[3]
    state_name = argv[4]

    if ';' not in state_name and '=' not in state_name:
        query = """SELECT cities.name FROM cities LEFT JOIN states
        ON cities.state_id = states.id WHERE states.name='{}'
        ORDER BY cities.id ASC""".format(state_name)
        db = MySQLdb.connect(
                host='localhost',
                user=username,
                password=pwd,
                database=db_name
                )
        cur = db.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        rows_count = len(rows)
        for row in rows:
            print("{}".format(row[0]), end="")
            if row != rows[rows_count - 1]:
                print(", ", end="")
        print()
        cur.close()
        db.close()
