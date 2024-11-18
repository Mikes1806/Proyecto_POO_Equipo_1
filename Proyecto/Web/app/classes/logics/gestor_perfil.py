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

            if df_mi_pefil.empty:
                self._add_info(df_mi_pefil)

                


            else:
              tab_mostrar_pefil, tab_modificacion_perfil = st.tabs(["Mi informacion", "Modificacion de informacion"])

              with tab_mostrar_pefil:
                self._add_row(df_mi_pefil)
              with tab_modificacion_perfil:
                self._modify_row(df_mi_pefil)

        except FileNotFoundError:
            st.error("Archivo CSV no encontrado. Por favor, verifica la ruta.")
            df_mi_pefil = pd.DataFrame(
                columns=[
                    "nombre_user", 
                    "ID_user", 
                    "monto_mensual", 
                    "edad", 
                    "telefono",
                    "correo_electronico",
                ]
            )
            st.dataframe(df_mi_pefil)

 def _add_info(self, df_mi_perfil):
    st.subheader("Agregar infomacion")
    nombre_user = st.text_input("Nombre completo")
    iD_user = st.text_input("ID del usuario")
    monto_mensual = st.text_input("Monto mensual")
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
                "monto_mensual": monto_mensual, 
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
                

 def _add_row(self, df_mi_perfil):
    st.write("Nombre ", df_mi_perfil ['nombre_user'][0])
    st.write("ID del usuario", df_mi_perfil ['ID_user'][0])
    st.write("Monto mensual", df_mi_perfil ['monto_mensual'][0])
    st.write("Edad", df_mi_perfil ['edad'][0])
    st.write("Numero telefonico", df_mi_perfil ['telefono'][0])
    st.write("Corre electronico", df_mi_perfil ['correo_electronico'][0])  

 def _modify_row(self, df_mi_perfil):

        st.subheader("Modificar infomacion")
        col1, col2 = st.columns(2)
        if not df_mi_perfil.empty:
            selected_index = 0

            if selected_index is not None:

                selected_record = df_mi_perfil.loc[selected_index]
                
                with col1:
                  nombre_user = st.text_input(
                     "Nombre ",
                      value=selected_record["nombre_user"],
                      key="nombre_user",
                    )

                  iD_user = st.text_input(
                      "ID de usuario",
                      value=selected_record["ID_user"],
                      key="ID_user",
                    )

                  monto_mensual = st.text_input(
                      "Monto mensual",
                      value=selected_record["monto_mensual"],
                      key="monto_mensual",
                    )
                
                with col2:
                   edad = st.text_input(
                       "Edad",
                      value=selected_record["edad"],
                      key="edad",
                    )

                   numero_telefono = st.text_input(
                      "Telefono",
                      value=selected_record["telefono"],
                      key="telefono",
                    )

                   correo_electronico = st.text_input(
                      "Correo electronico ",
                      value=selected_record["correo_electronico"],
                      key="correo_electronico",
                    )

                if st.button("Guardar Cambios", key="save_button"):
                 
                    df_mi_perfil.at[selected_index, "nombre_user"] = nombre_user
                    df_mi_perfil.at[selected_index, "ID_user"] = iD_user
                    df_mi_perfil.at[selected_index, "monto_mensual"] = monto_mensual
                    df_mi_perfil.at[selected_index, "edad"] = edad
                    df_mi_perfil.at[selected_index, "telefono"] = numero_telefono
                    df_mi_perfil.at[selected_index, "correo_electronico"] = correo_electronico

                    df_mi_perfil.to_csv(
                         "/usr/src/app/app/classes/logics/data/mi_perfil.csv",
                        mode="w",
                        index=False,
                    )

                    st.success("Registro modificado exitosamente.")
                    time.sleep(2)
                    st.experimental_rerun()
        else:
            st.error("No hay registros disponibles para modificar.")