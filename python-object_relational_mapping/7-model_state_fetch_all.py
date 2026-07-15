#!/usr/bin/python3
"""
Lists all State objects from the database 'hbtn_0e_6_usa'.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # 1. Grab arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # 2. Create the connection engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name
        ),
        pool_pre_ping=True
    )

    # 3. Create a configured "Session" class and instantiate it
    Session = sessionmaker(bind=engine)
    session = Session()

    # 4. Query all State objects, sort by id (ascending), and execute
    states = session.query(State).order_by(State.id.asc()).all()

    # 5. Print the results in the exact format: <id>: <name>
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # 6. Close the session to free up connection resources
    session.close()
