#!/usr/bin/env python3
""" set up basic flask app """
from flask import Flask, jsonify, request, abort
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


@app.route("/sessions", methods=['POST'], strict_slashes=False)
def login() -> Union[str, tuple]:
    """ create a session """
    email = request.form['email']
    password = request.form['password']

    if not AUTH.valid_login(email, password):
        abort(401)
    sess_id = AUTH.create_session(email)
    resp = jsonify({"email": email, "message": "logged in"})
    resp.set_cookie("session_id", sess_id)
    return resp


@app.route("/sessions", methods=['DELETE'], strict_slashes=False)
def logout() -> Union[str, tuple]:
    """ implement logout """
    session_id = request.cookies.get('session_id', None)
    user = AUTH.get_user_from_session_id(session_id)
    if session_id is None or user is None:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect('/')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
