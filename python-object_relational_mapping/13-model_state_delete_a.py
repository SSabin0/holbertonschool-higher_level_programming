#!/usr/bin/python3
"""Module to delete all States with a name containing 'a'."""
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

    for state in session.query(State).filter(State.name.contains("a")):
        session.delete(state)

    session.commit()
    session.close()
