#!/usr/bin/python3
"""Select all cities from database with their states
"""
import sys

from sqlalchemy.orm import aliased, sessionmaker
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine, select, Subquery

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = select(City)
    city_obj = session.scalars(query).all()
    for city in city_obj:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))
