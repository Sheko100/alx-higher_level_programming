#!/usr/bin/python3
"""Module to select a state row by name the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    username, pwd, db_name = argv[1], argv[2], argv[3]

    query = """SELECT cities.id, cities.name, states.name FROM cities
    INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC
    """
    db = MySQLdb.connect(
            host='localhost',
            user=username,
            password=pwd,
            database=db_name
            )
    cur = db.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
