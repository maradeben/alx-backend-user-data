#!/usr/bin/env python3
""" Session Authentication implementation """
from api.v1.auth.auth import Auth
import uuid

class SessionAuth(Auth):
    """ The session auth class """

    user_id_by_session_id = {}
    
    def create_session(self, user_id: str = None) -> str:
        """ create session id for a user id """

        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = uuid.uuid4()
        self.user_id_by_session_id[session_id] = user_id
