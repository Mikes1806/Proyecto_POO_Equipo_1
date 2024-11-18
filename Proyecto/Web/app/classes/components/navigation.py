import time
from datetime import datetime

import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

from ..logics.gestor_perfil import Gestorperfil
from ..logics.gestor_contactos import GestorContactos


class Navigation:
    def __init__(self) -> None:
        self._init_title = "Gestion de perfil"

        self._menu_handlers = {
            "Mi perfil": self._handle_Gestion_de_perfil,
            "Gestion ingresos fijos": self._handle_gestion_de_contactos,
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
                    "box-arrow-left",
                ],
                menu_icon="cast",
                default_index=0,
            )

        handler = self._menu_handlers.get(option)
        if handler:
            handler()

    def _handle_Gestion_de_perfil(self):
        st.title( self._init_title)
        with st.spinner("Wait for it..."):
            Gestorperfil().logic()


    def _handle_gestion_de_contactos(self):
        st.title("Gestion De Contactos")
        with st.spinner("Wait for it..."):
            GestorContactos().logic()


    def logout(self):
        st.session_state["logged_in"] = False
        st.experimental_rerun()
