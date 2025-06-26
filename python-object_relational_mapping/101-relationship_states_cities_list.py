#!/usr/bin/python3
"""List all states and their cities using relationship"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    session = Session(engine)

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
        for city in sorted(state.cities, key=lambda c: c.id):
            print(f"\t{city.id}: {city.name}")

    session.close()
