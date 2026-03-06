#!/usr/bin/python3
""" adds "Louisiana" to the database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, insert

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@172.17.0.4/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    with engine.connect() as conn:
        query = insert(State).values(name="Louisiana")

        query.compile()
        i = conn.execute(query)
        if i is None:
            print("Not found")
        else:
            print("{}".format(i.inserted_primary_key[0]))
