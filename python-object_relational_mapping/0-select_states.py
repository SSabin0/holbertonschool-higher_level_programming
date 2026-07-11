#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    
    # Create a cursor object
    cursor = db.cursor()
    
    # Execute the query
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    
    # Fetch and print results
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        
    # Close resources
    cursor.close()
    db.close()
