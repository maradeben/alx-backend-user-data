#!/usr/bin/env python3
""" implement the BasicAuth class """
from api.v1.auth.auth import Auth
import base64


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
