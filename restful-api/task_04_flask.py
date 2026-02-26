#!/usr/bin/python3
from flask import Flask, jsonify, request
from werkzeug.exceptions import BadRequest


app = Flask(__name__)

# change this to empty dictionary before pushing
users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}


@app.route("/")
def home():
    return "Welcome to the Flask API!", 200


@app.route("/data")
def data():
    user_keys = list(users.keys())
    return jsonify(user_keys), 200


@app.route("/status")
def status():
    return "OK", 200


@app.route("/users/<username>")
def show_user(username):
    user = users.get(username)

    if not user:
        return {"error": "User not found"}, 404

    return jsonify(user), 200


@app.route("/add_user", methods=['POST'])
def add_user():
    try:
        valid_data = request.json
        user_key = valid_data.get("username")
        if not user_key:
            return {"error": "Username is required"}, 400
        check_user = users.get(user_key)
        if check_user:
            return {"error": "Username already exists"}, 409
        users[user_key] = valid_data
        response = {
            "message": "User added",
            "user": users[user_key]
        }
        return jsonify(response), 201

    except BadRequest:
        return {"error": "Invalid JSON"}, 400


if __name__ == "__main__":
    app.run()
