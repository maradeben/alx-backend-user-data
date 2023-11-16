#!/usr/bin/env python3
""" set up basic flask app """
from flask import Flask, jsonify, request
from auth import Auth
from typing import Union


app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'], strict_slashes=False)
def message():
    """ base route with message """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'], strict_slashes=False)
def users() -> Union[str, tuple]:
    """ post endpoint for users """
    email = request.form['email']
    password = request.form['password']

    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    else:
        return jsonify({"email": "{}".format(email),
                       "message": "user created"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
