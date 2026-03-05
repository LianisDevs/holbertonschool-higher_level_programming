#!/usr/bin/python3
"""
This module contains the get_cities_by_state function
"""

import sys
import MySQLdb


def get_cities_by_state():
    """
    This function connects to a MySQL db
    Performs SQL query to select states and cities
    Prints each row from selection
    """
    my_db = MySQLdb.connect(
        host='127.0.0.1',
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3],
        port=3307
    )

    cur = my_db.cursor()

    cur.execute("SELECT c.id, c.name, s.name \
        FROM cities AS c \
        LEFT JOIN states as s \
        ON c.state_id = s.id;")

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    my_db.close()


if __name__ == "__main__":
    get_cities_by_state()
