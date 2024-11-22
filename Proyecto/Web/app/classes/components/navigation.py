import time
from datetime import datetime
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
from ..logics.gestor_perfil import Gestorperfil
from ..logics.gastos_fijos import Gestor_gastos_fijos
from ..logics.gastos_imprevistos import Gestor_gastos_imprevistos


class Navigation:

    def __init__(self) -> None:
        self._init_title = "Gestión de Perfil"
        self._menu_handlers = {
            "Mi perfil": self._handle_Gestion_de_perfil,
            "Gastos Fijos": self._handle_Gastos_fijos,
            "Gastos Imprevistos": self._handle_Gastos_imprevistos,
            "Cerrar sesión": self.logout,
        }
        self._options = list(self._menu_handlers.keys())

    def render_menu(self) -> None:
        with st.sidebar:
            option = option_menu(
                "Menú",
                self._options,
                icons=[
                    "person-circle",
                    "credit-card",
                    "bag-fill",
                    "box-arrow-left",
                ],
                menu_icon="brilliance",
                default_index=0,
            )
        handler = self._menu_handlers.get(option)
        if handler:
            handler()

    def _handle_Gestion_de_perfil(self) -> None:
        st.title( self._init_title)
        with st.spinner("Wait for it..."):
            Gestorperfil().logic()

    def _handle_Gastos_fijos(self) -> None:
        st.title("Gastos fijos")
        with st.spinner("Wait for it..."):
            Gestor_gastos_fijos().logic()

    def _handle_Gastos_imprevistos(self) -> None:
        st.title("Gastos imprevistos")
        with st.spinner("Wait for it..."):
            Gestor_gastos_imprevistos().logic()

    def logout(self) -> None:
        st.session_state["logged_in"] = False
        st.experimental_rerun()
