#!/usr/bin/python3
import sys
import MySQLdb


def lists_from_database():
    my_db = MySQLdb.connect(
        host='127.0.0.1',
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3],
        port=3306
    )

    cur = my_db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    my_db.close()


if __name__ == "__main__":
    lists_from_database()
