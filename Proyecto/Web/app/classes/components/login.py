import streamlit as st


class Login:

    def __init__(self, username:str, password:str) -> None:
        self._username = username
        self._password = password
        self._users = {"misa93149": "12345"}

    def validation_credentials(self) -> bool:
        if (self._username in self._users) and (self._users[self._username] == self._password):
            return True
        else:
            return False
