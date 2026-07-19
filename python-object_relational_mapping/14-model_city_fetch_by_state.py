#!/usr/bin/python3
"""Script that lists all cities with their state name."""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}"
        f"@localhost:3306/{sys.argv[3]}",
        pool_pre_ping=True
    )
    Session = sessionmaker(engine)
    session = Session()

    results = session.query(City, State).filter(
        City.state_id == State.id
    ).order_by(City.id)

    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
