#!/usr/bin/python3
"""Select all states from datatbase
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, select

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    query = select(State)
    result = engine.execute(query)
    for i in result.fetchall():
        print("{}: {}".format(i[0], i[1]))
