#!/usr/bin/python3
"""Select first row from states from database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, select

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    with engine.connect() as conn:
        query = select(State)

        i = conn.execute(query).first()
        if i is None:
            print("Nothing")

        else:
            print("{}: {}".format(i[0], i[1]))
