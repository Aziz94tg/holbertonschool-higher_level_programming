#!/usr/bin/python3
"""
Creates the State "California" with City "San Francisco"
in the database hbtn_0e_100_usa using ORM.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import State, Base
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    session = Session(engine)

    california = State(name="California")
    san_francisco = City(name="San Francisco")
    california.cities.append(san_francisco)

    session.add(california)
    session.commit()

    session.close()
