#!/usr/bin/python3
"""Module to fetch a state by exact name."""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}"
        f"@localhost:3306/{sys.argv[3]}",
        pool_pre_ping=True
    )
    Session = sessionmaker(engine)
    session = Session()

    state = session.query(State).filter(State.name == sys.argv[4]).first()

    if state is None:
        print("Not found")
    else:
        print(f"{state.id}")
