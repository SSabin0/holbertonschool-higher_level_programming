from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, 
    get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# User storage
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# Basic Auth verification
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None

# Custom JWT error handlers
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

# Role-based decorator
def admin_required(fn):
    @wraps(fn)
    @jwt_required()
    def wrapper(*args, **kwargs):
        claims = get_jwt()
        if claims.get("role") == "admin":
            return fn(*args, **kwargs)
        else:
            return jsonify({"error": "Admin access required"}), 403
    return wrapper

# Routes
@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    if username in users and check_password_hash(users[username]["password"], password):
        access_token = create_access_token(
            identity=username, 
            additional_claims={"role": users[username]["role"]}
        )
        return jsonify({"access_token": access_token}), 200
    
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

@app.route('/admin-only', methods=['GET'])
@admin_required
def admin_only():
    return "Admin Access: Granted"

if __name__ == '__main__':
    app.run(port=5000)
