#!/usr/bin/python3
"""lists all states from database containing "a"
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, select

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    with engine.connect() as conn:
        query = select(State).filter(State.name.contains("a"))

        for i in conn.execute(query):
            print("{}: {}".format(i[0], i[1]))
