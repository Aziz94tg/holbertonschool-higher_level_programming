#!/usr/bin/python3
"""
Adds the State object 'Louisiana' to the database.
Usage: ./11-model_state_insert.py
<username> <password> <database>
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]
        ), pool_pre_ping=True
    )

    session = Session(engine)

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()
