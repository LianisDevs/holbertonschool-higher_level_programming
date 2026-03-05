#!/usr/bin/python3
"""
This module contains the states_N_from_database function
"""

import sys
import MySQLdb


def states_N_from_database():
    """
    This function connects to a MySQL db
    Performs SQL query to select states starting with N from the table
    Prints each row from selection
    """
    my_db = MySQLdb.connect(
        host='127.0.0.1',
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3],
        port=3306
    )

    cur = my_db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    my_db.close()


if __name__ == "__main__":
    states_N_from_database()
