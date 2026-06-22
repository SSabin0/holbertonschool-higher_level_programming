#!/usr/bin/env python3
"""
Module for converting CSV data to JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Converts a CSV file to a JSON file named data.json.
    
    Returns True if successful, False if the file is not found or an error occurs.
    """
    try:
        # 1. Open the CSV file and read it into a list of dictionaries
        with open(csv_filename, mode="r", encoding="utf-8") as f:
            data = list(csv.DictReader(f))

        # 2. Open "data.json" and dump the data variable into it
        with open("data.json", mode="w", encoding="utf-8") as f:
            json.dump(data, f)
            
        # If both blocks complete without crashing, return True
        return True

    except FileNotFoundError:
        # If the file doesn't exist, catch the error and return False
        return False
    except Exception:
        # Catch any other unexpected error just in case
        return False
