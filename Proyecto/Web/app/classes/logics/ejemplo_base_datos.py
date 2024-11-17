import streamlit as st
import pandas as pd
import time
from datetime import datetime
import psycopg2


class EjemploBaseDatos:
    def __init__(self) -> None:

        self._conn = psycopg2.connect(
            host="172.29.0.3",
            port="5432",
            database="postgres",
            user="josue",
            password="1234",
        )

    def logic(self):

        try:

            query = "SELECT * FROM tbl_maintenance"

            df_ejemplo = pd.read_sql(query, self._conn)

            st.subheader("Ejemplo Base De Datos")
            st.dataframe(df_ejemplo)
            st.markdown("<br>", unsafe_allow_html=True)
            st.divider()
            st.markdown("<br>", unsafe_allow_html=True)

        except FileNotFoundError:
            st.error("Archivo CSV no encontrado. Por favor, verifica la ruta.")
            df_ejemplo = pd.DataFrame(
                columns=[
                    "name",
                    "telefono",
                ]
            )
            st.dataframe(df_ejemplo)
