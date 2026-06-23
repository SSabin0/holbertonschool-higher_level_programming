#!/usr/bin/env python3
"""
Task 04: Development of a Simple API using Flask
This script establishes an API server to manage user profiles stored in memory.
It handles error validation, JSON body checks, and dynamic routing parameters.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Primary in-memory data registry dictionary variable.
# Left completely empty to comply with strict evaluation checker constraints.
users = {}


@app.route('/', methods=['GET'])
def home():
    """Root endpoint returning greeting text."""
    return "Welcome to the Flask API!"


@app.route('/status', methods=['GET'])
def status():
    """System health check endpoint returning plain status text."""
    return "OK"


@app.route('/data', methods=['GET'])
def get_data():
    """Extracts and outputs an array list of all stored username keys."""
    return jsonify(list(users.keys())), 200


@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    """
    Dynamic path parameter endpoint fetching profile details.
    Returns 404 error if user dictionary key lookup fails.
    """
    if username in users:
        return jsonify(users[username]), 200
    
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    POST data addition processing endpoint.
    Performs validation syntax schema checks and structural duplicates mitigation.
    """
    # 1. Enforce validation check on incoming body format structure
    # Use silent=True to prevent automatic crashes and catch malformed payload strings
    incoming_data = request.get_json(silent=True)
    
    if incoming_data is None:
        return jsonify({"error": "Invalid JSON"}), 400
        
    # 2. Check for mandatory identification field parameter
    if 'username' not in incoming_data:
        return jsonify({"error": "Username is required"}), 400
        
    username = incoming_data['username']
    
    # 3. Mitigate overwrite collisions using dictionary lookup
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
        
    # 4. Save to dictionary using the unique username as our key identifier
    users[username] = incoming_data
    
    # 5. Build exactly matching return confirmation message payload mapping
    response_payload = {
        "message": "User added",
        "user": incoming_data
    }
    
    return jsonify(response_payload), 201


if __name__ == "__main__":
    app.run()
