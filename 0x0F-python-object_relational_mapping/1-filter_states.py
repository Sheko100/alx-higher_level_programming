#!/usr/bin/python3
"""Module to select states with name started with 'N' from
the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    username, pwd, db_name = argv[1], argv[2], argv[3]
    try:
        db = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=username,
                password=pwd,
                db=db_name,
                charset='utf8'
                )
        cur = db.cursor()
        cur.execute("""SELECT * FROM states WHERE name LIKE UPPER('N%')
                ORDER BY states.id ASC""")
        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        db.close()
    except Exception as e:
        print(e)
