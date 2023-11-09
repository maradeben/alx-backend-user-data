#!/usr/bin/env python3
""" Initializing the Auth module """
from flask import request
from typing import List, TypeVar


class Auth:
    """ authenticator class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ determine paths requiring auth """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        path+='/' if not path.endswith('/') else ''
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """ return None for starters """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ return None for starters """
        return None
