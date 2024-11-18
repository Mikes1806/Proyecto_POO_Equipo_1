import streamlit as st
import pandas as pd
import time
from datetime import datetime

class Gestorperfil:
 def __init__(self) -> None:

    pass

 def logic(self):

        try:

            df_mi_pefil = pd.read_csv(
                "/usr/src/app/app/classes/logics/data/mi_perfil.csv"
            )
            st.subheader("Perfil")
            st.dataframe(df_mi_pefil)
            st.markdown("<br>", unsafe_allow_html=True)
            st.divider()
            st.markdown("<br>", unsafe_allow_html=True)

            tab_agregar_pefil, tab_modificacion_perfil = st.tabs(["Agregar informacion", "Modificacion de informacion"])

            with tab_agregar_pefil:
                self._add_row(df_mi_pefil)
            #with tab_modificacion_perfil:
             #   self._modify_row(df_mi_pefil)

        except FileNotFoundError:
            st.error("Archivo CSV no encontrado. Por favor, verifica la ruta.")
            df_mi_pefil = pd.DataFrame(
                columns=[
                    "nombre_user", 
                    "ID_user", 
                    "monto_mensaul", 
                    "edad", 
                    "telefono",
                    "correo_electronico",
                ]
            )
            st.dataframe(df_mi_pefil)

 def _add_row(self, df_mi_perfil):
        
        st.subheader("Agregar infomacion")

        nombre_user = st.text_input("Nombre completo")
        iD_user = st.text_input("ID del usuario")
        monto_mensual = st.text_input("Monto mensaul")
        edades = list(range(18, 120))
        edad_seleccionada = st.selectbox(
        "Selecciona tu edad:",
        edades,
        )
        numero_telefono = st.text_input("Numero telefonico")
        correo_electronico = st.text_input("Corre electronico")

        if st.button("Agregar infomacion"):

            new_record = {
                "nombre_user": nombre_user , 
                "ID_user": iD_user, 
                "monto_mensaul": monto_mensual, 
                "edad": edad_seleccionada, 
                "telefono": numero_telefono,
                "correo_electronico": correo_electronico,
            }

            df_mi_perfil = df_mi_perfil.append(new_record, ignore_index=True)
            df_mi_perfil.to_csv(
                "/usr/src/app/app/classes/logics/data/mi_perfil.csv",
                mode="w",
                index=False,
                )
            st.success("Registro agregado exitosamente.")
            time.sleep(5)
            st.experimental_rerun()

 def _modify_row(self, df_mi_perfil):
    pass
   

    