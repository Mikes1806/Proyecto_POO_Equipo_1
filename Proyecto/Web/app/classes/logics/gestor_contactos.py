import streamlit as st
import pandas as pd
import time
from datetime import datetime


class GestorContactos:
    def __init__(self) -> None:
        pass

    def logic(self):

        try:

            df_contactos = pd.read_csv(
                "/usr/src/app/app/classes/logics/data/contactos.csv"
            )
            st.subheader("Agenda")
            st.dataframe(df_contactos)
            st.markdown("<br>", unsafe_allow_html=True)
            st.divider()
            st.markdown("<br>", unsafe_allow_html=True)

            tab_agregacion, tab_modificacion = st.tabs(["Agregación", "Modificacion"])

            with tab_agregacion:
                self._add_row(df_contactos)
            with tab_modificacion:
                self._modify_row(df_contactos)

        except FileNotFoundError:
            st.error("Archivo CSV no encontrado. Por favor, verifica la ruta.")
            df_contactos = pd.DataFrame(
                columns=[
                    "name",
                    "telefono",
                ]
            )
            st.dataframe(df_contactos)

    def _add_row(self, df_contactos):
        st.subheader("Agregar nuevo registro")

        nombre_contacto = st.text_input("Nombre del contacto")
        numero_contacto = st.text_input("Numero del contacto")
        fecha_alta = st.date_input("Fecha de alta contacto", value=datetime.now())

        if st.button("Agregar Registro"):

            fecha_alta = fecha_alta.strftime("%d/%m/%y")

            new_record = {
                "nombre_contacto": nombre_contacto,
                "numero_contacto": numero_contacto,
                "fecha_alta": fecha_alta,
            }

            df_contactos = df_contactos.append(new_record, ignore_index=True)
            df_contactos.to_csv(
                "/usr/src/app/app/classes/logics/data/contactos.csv",
                mode="w",
                index=False,
            )
            st.success("Registro agregado exitosamente.")
            time.sleep(5)
            st.experimental_rerun()

    def _modify_row(self, df_contactos):

        st.subheader("Modificar Registro Existente")

        if not df_contactos.empty:
            selected_index = st.selectbox(
                "Selecciona el índice del registro a modificar", df_contactos.index
            )

            if selected_index is not None:

                selected_record = df_contactos.loc[selected_index]

                nombre_contacto = st.text_input(
                    "Nombre del contacto",
                    value=selected_record["nombre_contacto"],
                    key="nombre_contacto",
                )

                numero_contacto = st.text_input(
                    "Numero del contacto",
                    value=selected_record["numero_contacto"],
                    key="numero_contacto",
                )

                fecha_alta = st.date_input(
                    "Fecha de alta contacto",
                    value=datetime.strptime(selected_record["fecha_alta"], "%d/%m/%y"),
                    key="fecha_alta",
                )

                if st.button("Guardar Cambios", key="save_button"):

                    fecha_alta = fecha_alta.strftime("%d/%m/%y")

                    df_contactos.at[selected_index, "nombre_contacto"] = nombre_contacto
                    df_contactos.at[selected_index, "numero_contacto"] = numero_contacto
                    df_contactos.at[selected_index, "fecha_alta"] = fecha_alta

                    df_contactos.to_csv(
                        "/usr/src/app/app/classes/logics/data/contactos.csv",
                        mode="w",
                        index=False,
                    )

                    st.success("Registro modificado exitosamente.")
                    time.sleep(2)
                    st.experimental_rerun()
        else:
            st.error("No hay registros disponibles para modificar.")
