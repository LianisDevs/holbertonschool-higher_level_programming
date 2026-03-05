#!/usr/bin/python3
"""
This module contains the get_cities_from_user_input function
"""

import sys
import MySQLdb


def get_cities_from_user_input():
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

    user_input = sys.argv[4]

    sql_query = "SELECT c.name \
                FROM cities as c \
                WHERE c.state_id = ( \
                    SELECT s.id \
                    FROM states as s \
                    WHERE s.name = %s)"

    cur.execute(sql_query, (user_input,))

    query_rows = cur.fetchall()

    row_array = []
    for row in query_rows:
        row_array.append(row[0])

    cities = ", ".join(row_array)

    print(cities)
    cur.close()
    my_db.close()


if __name__ == "__main__":
    get_cities_from_user_input()
