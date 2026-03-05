#!/usr/bin/python3
"""
This module contains the get_user_input_from_database function
"""

import sys
import MySQLdb


def get_user_input_from_database():
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

    sql_query = "SELECT * FROM states \
        WHERE name COLLATE utf8mb4_bin  = %s"

    cur.execute(sql_query, (user_input,))

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    my_db.close()


if __name__ == "__main__":
    get_user_input_from_database()
