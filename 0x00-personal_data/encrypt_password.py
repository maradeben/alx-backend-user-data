#!/usr/bin/env python3
"""
password encypting module using bcrypt
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ hash and return hashed password """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ reverse check if password matches the hatched """
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid
