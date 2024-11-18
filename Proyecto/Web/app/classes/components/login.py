import streamlit as st


class Login:
    def __init__(self, username, password) -> None:
        self._username = username
        self._password = password
        self._users = {"Landa": "123"}

    def validation_credentials(
        self,
    ):

        if (self._username in self._users) and (
            self._users[self._username] == self._password
        ):
            return True
        else:
            return False
