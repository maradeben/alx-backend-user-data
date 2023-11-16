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


@app.route("/profile", methods=['GET'], strict_slashes=False)
def profile() -> str:
    """ implement a profile function """
    session_id = request.cookies.get('session_id', None)
    user = AUTH.get_user_from_session_id(session_id)
    if session_id is None or user is None:
        abort(403)
    return jsonify({"email": user.email}), 200


@app.route("/reset_password", methods=['POST'], strict_slashes=False)
def get_reset_password_token() -> str:
    """ get token to reset password """
    email = request.form.get('email', None)
    if email is None:
        abort(403)
    try:
        token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)

    return jsonify({"message": email, "reset_token": token}) 200


@app.route("/reset_password", methods=['PUT'], strict_slashes=False)
def update_password() -> str:
    """ updaet new password """
    email = request.form.get('email', None)
    reset_token = request.form.get('reset_token', None)
    new_password = request.form.get('new_password', None)

    if email is None or reset_token is None or new_password is None:
        return None

    try:
        token = AUTH.update_password(reset_token, new_password)
    except ValueError:
        abort(403)

    return jsonify({"email": email, "message": "Password updated"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
