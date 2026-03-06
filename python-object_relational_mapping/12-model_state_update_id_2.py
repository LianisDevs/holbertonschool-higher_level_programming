#!/usr/bin/python3
""" changes the name of a State object from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, update

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    with engine.connect() as conn:
        query = update(State).where(State.id == 2).values(name="New Mexico")

        query.compile()
        i = conn.execute(query)
        conn.commit()
