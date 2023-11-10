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

        session_id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ return user id based on session id """
        if not session_id or not isinstance(session_id, str):
            return None
        return SessionAuth.user_id_by_session_id.get(session_id)
