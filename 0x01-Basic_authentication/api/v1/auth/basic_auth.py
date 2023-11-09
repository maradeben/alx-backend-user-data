#!/usr/bin/env python3
""" implement the BasicAuth class """
from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """ BasicAuth class inheriting from Auth """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ return Base64 parth of Authorization header for
            a Basic Authentication
        """
        if authorization_header is not None and\
                isinstance(authorization_header, str) and\
                authorization_header.startswith("Basic "):
            return authorization_header.split()[1]
        return None

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """ return decoded value of the Base64 string """
        if base64_authorization_header is not None and\
                isinstance(base64_authorization_header, str):
            try:
                return base64.b64decode(base64_authorization_header,
                                        validate=True).decode('utf-8')
            except Exception as e:
                return None
        return None

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> (str, str):
        """ extract user email and password from Base64 decoded value """
        if decoded_base64_authorization_header is not None and\
                isinstance(decoded_base64_authorization_header, str) and\
                ':' in decoded_base64_authorization_header:
            email, password = decoded_base64_authorization_header.split(':')
            return email, password
        return None

    def user_object_from_credentials(self, user_email: str, user_pwd: str
                                     ) -> TypeVar('User'):
        """ get user credentials and return User instance """
        if user_email is None or not isinstance(user_email, str)\
                or user_pwd is None or not isinstance(user_pwd, str):
            return None
        user = User.search({"email": user_email})
        if user == []:
            return None
        else:
            user = user[0]
        return user if user.is_valid_password(user_pwd) else None
