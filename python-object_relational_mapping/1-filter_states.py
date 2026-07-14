#!/usr/bin/python3
<<<<<<< HEAD
"""Script that lists all states with a name starting with N."""
import MySQLdb
import sys

=======
"""Module for Filtering states that start with N"""

import MySQLdb
import sys


>>>>>>> 03d1939c638c2b730bc04f90128154386ac2e88c
if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cur = conn.cursor()
<<<<<<< HEAD
    cur.execute("SELECT id, name FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC")
=======
    cur.execute(
        "SELECT * "
        "FROM states WHERE name LIKE BINARY 'N%' "
        "ORDER BY id ASC"
    )
>>>>>>> 03d1939c638c2b730bc04f90128154386ac2e88c
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
