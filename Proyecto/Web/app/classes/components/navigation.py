import time
from datetime import datetime

import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

from ..logics.gestor_contactos import GestorContactos
from ..logics.ejemplo_base_datos import EjemploBaseDatos


class Navigation:
    def __init__(self) -> None:
        self._init_title = "POO 1355"
        self._init_secondtitle = "MAC"

        self._menu_handlers = {
            "Inicio": self._handle_inicio,
            "Gestion Contactos": self._handle_gestion_de_contactos,
            "Ejemplo Base Datos": self._handle_ejemplo_base_datos,
            "Cerrar sesión": self.logout,
        }

        self._options = list(self._menu_handlers.keys())

    def render_menu(self):

        with st.sidebar:
            option = option_menu(
                "Main Menu",
                self._options,
                icons=[
                    "house",
                    "gear",
                    "gear",
                    "box-arrow-left",
                ],
                menu_icon="cast",
                default_index=0,
            )

        handler = self._menu_handlers.get(option)
        if handler:
            handler()

    def _handle_inicio(self):
        st.title(self._init_title)
        st.write(self._init_secondtitle)

    def _handle_gestion_de_contactos(self):
        st.title("Gestion De Contactos")
        with st.spinner("Wait for it..."):
            GestorContactos().logic()

    def _handle_ejemplo_base_datos(self):
        EjemploBaseDatos().logic()

    def logout(self):
        st.session_state["logged_in"] = False
        st.experimental_rerun()
