#!/usr/bin/python3

from flask import Flask, json, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, current_user, get_jwt_identity, jwt_required, JWTManager

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "icecream"
app.config['JWT_TOKEN_LOCATION'] = 'headers'
jwt = JWTManager(app)
auth = HTTPBasicAuth()
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted", 200


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    user = verify_password(username, password)
    if user:
        access_token = create_access_token(identity=user)
        return jsonify(access_token=access_token)


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    current_user = get_jwt_identity()
    response = {
        "message": "JWT Auth: Access Granted"
    }
    return jsonify(response) , 200


@app.route("/admin-only")
@jwt_required()
def admin_access():
    # check if jwc you're given belongs to admin
    current_username = get_jwt_identity()
    # gets the full user obj
    user = users.get(current_username)

    #check role on user for admin
    if user and user["role"] == "admin":
        response = {
            "message": "Admin Access: Granted"
        }
        return jsonify(response), 200

    response = {
        "error":  "Admin access required"
    }
    return jsonify(response), 403


@jwt.invalid_token_loader
def invalid_token_handler(jwt_header):
    response = {
        "error": "Invalid token"
    }
    return jsonify(response), 401


@jwt.unauthorized_loader
def unauthorized_token_handler(err):
    response = {
        "error": "Missing or invalid token"
    }
    return jsonify(response), 401


@jwt.expired_token_loader
def expired_token_handler(err):
    response = {
        "error": "Token has expired"
    }
    return jsonify(response), 401


@jwt.revoked_token_loader
def revoked_token_handler(err):
    response = {
        "error": "Token has been revoked"
    }
    return jsonify(response), 401


@jwt.needs_fresh_token_loader
def need_fresh_token_handler(err):
    response = {
        "error": "Fresh token required"
    }
    return jsonify(response), 401


if __name__ == '__main__':
    app.run()
