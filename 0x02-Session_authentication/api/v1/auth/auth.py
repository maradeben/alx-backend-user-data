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

        for ex_path in excluded_paths:
            if ex_path.endswith('*') and path.startswith(ex_path[:-1]):
                return False

        path += '/' if not path.endswith('/') else ''
        # return True if path is not path of the excluded
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """ return None for starters """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ return None for starters """
        return None
