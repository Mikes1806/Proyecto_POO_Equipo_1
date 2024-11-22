import streamlit as st
import pandas as pd
import time
from datetime import datetime


class Gestorperfil:

    def __init__(self) -> None:
        pass

    def logic(self) -> None:
        try:
            df_mi_pefil = pd.read_csv("/usr/src/app/app/classes/logics/data/mi_perfil.csv")
            #st.subheader("Perfil")
            #st.dataframe(df_mi_pefil)
            #st.markdown("<br>", unsafe_allow_html=True)
            #st.divider()
            #st.markdown("<br>", unsafe_allow_html=True)
            if df_mi_pefil.empty:
                self._add_info(df_mi_pefil)
            else:
                tab_mostrar_pefil, tab_modificacion_perfil = st.tabs(["Mi información", "Modificación de información"])
                with tab_mostrar_pefil:
                    self._displey_perfil(df_mi_pefil)
                with tab_modificacion_perfil:
                    self._modify_row(df_mi_pefil)
        except FileNotFoundError:
            st.error("Archivo CSV no encontrado. Por favor, verifíca la ruta.")
            df_mi_pefil = pd.DataFrame(
                columns=[
                    "nombre_user",
                    "edad", 
                    "telefono",
                    "correo_electronico",
                    "monto_mensual",
                    "monto_mensual_extra", 
                ]
            )
            st.dataframe(df_mi_pefil)

    def _add_info(self, df_mi_perfil:list) -> None:
        st.subheader("Agregar infomación")
        nombre_user = st.text_input("Nombre")
        edades = list(range(18, 120))
        edad_seleccionada = st.selectbox("Selecciona tu edad:", edades)
        numero_telefono = st.text_input("Número telefónico")
        correo_electronico = st.text_input("Correo electrónico")
        monto_mensual = st.text_input("Monto mensual")
        if not monto_mensual.replace('.', '', 1).isdigit():
            st.error("El monto mensual debe ser un número.")
        else:
            monto_mensual = float(monto_mensual)
        monto_mensual_extra = st.text_input("Monto mensual extra")
        if not monto_mensual_extra.replace('.', '', 1).isdigit():
            st.error("El monto mensual extra debe ser un número.")
        else:
            monto_mensual_extra = float(monto_mensual_extra)
        if st.button("Agregar infomación"):
                new_record = {
                    "nombre_user": nombre_user, 
                    "edad": edad_seleccionada, 
                    "telefono": numero_telefono,
                    "correo_electronico": correo_electronico,
                    "monto_mensual": monto_mensual,
                    "monto_mensual_extra": monto_mensual_extra,
                }
                df_mi_perfil = df_mi_perfil.append(new_record, ignore_index=True)
                df_mi_perfil.to_csv(
                    "/usr/src/app/app/classes/logics/data/mi_perfil.csv",
                    mode="w",
                    index=False,
                    )
                st.success("Perfil agregado exitosamente.")
                time.sleep(3)
                st.experimental_rerun()
                
    def _eliminar_perfil(self, df_mi_perfil:list) -> None:
        csv_file = '/usr/src/app/app/classes/logics/data/mi_perfil.csv'
        selected_index = 0
        df_mi_perfil = df_mi_perfil.drop(selected_index).reset_index(drop=True)
        df_mi_perfil.to_csv(csv_file, index=False)    
        st.success("Perfil eliminado exitosamente.")
        time.sleep(3)
        st.experimental_rerun()

    def _displey_perfil(self, df_mi_perfil:list) -> None:
        nombre_user = df_mi_perfil ['nombre_user'][0]
        edad_seleccionada = df_mi_perfil ['edad'][0]
        numero_telefono = df_mi_perfil ['telefono'][0]
        correo_electronico = df_mi_perfil ['correo_electronico'][0]
        monto_mensual = df_mi_perfil ['monto_mensual'][0]
        monto_mensual_extra = df_mi_perfil ['monto_mensual_extra'][0]
        st.write("Nombre del usuario")
        st.markdown(
            f"""
            <div style="
                border: 2px solid white; 
                border-radius: 10px; 
                padding: 2px; 
                background-color: #151516;">
                <p style='color: white;'>  {nombre_user}</p>
            </div>
            """,
            unsafe_allow_html=True
            )
        st.write("")
        st.write("Edad")
        st.markdown(
            f"""
            <div style="
                border: 2px solid white; 
                border-radius: 10px; 
                padding: 2px;
                background-color: #151516;">
                <p style='color: white;'>  {edad_seleccionada}</p>
            </div>
            """,
            unsafe_allow_html=True
            )
        st.write("") 
        st.write("Número de teléfono")
        st.markdown(
            f"""
            <div style="
                border: 2px solid white; 
                border-radius: 10px; 
                padding: 2px;
                background-color: #151516;">
                <p style='color: white;'>  {numero_telefono}</p>
            </div>
            """,
            unsafe_allow_html=True
            )
        st.write("") 
        st.write("Correo electrónico")
        st.markdown(
            f"""
            <div style="
                border: 2px solid white; 
                border-radius: 10px; 
                padding: 2px;
                background-color: #151516;">
                <p style='color: white;'>  {correo_electronico}</p>
            </div>
            """,
            unsafe_allow_html=True
            )
        st.write("")
        st.write("Monto mensual")
        st.markdown(
            f"""
            <div style="
                border: 2px solid white; 
                border-radius: 10px; 
                padding: 2px; 
                background-color: #151516;">
                <p style='color: white;'>  {monto_mensual}</p>
            </div>
            """,
            unsafe_allow_html=True
            )
        st.write("")
        st.write("Monto mensual extra")
        st.markdown(
            f"""
            <div style="
                border: 2px solid white; 
                border-radius: 10px; 
                padding: 2px; 
                background-color: #151516;">
                <p style='color: white;'>  {monto_mensual_extra}</p>
            </div>
            """,
            unsafe_allow_html=True
            )
        st.write("")
        if st.button('Eliminar información'):
            self._eliminar_perfil(df_mi_perfil)

    def _modify_row(self, df_mi_perfil:list) -> None:
        #st.subheader("Modificar mi información")
        col1, col2 = st.columns(2)
        if not df_mi_perfil.empty:
            selected_index = 0
            if selected_index is not None:
                selected_record = df_mi_perfil.loc[selected_index]
                with col1:
                    nombre_user = st.text_input(
                        "Nombre",
                        value=selected_record["nombre_user"],
                        key="nombre_user",
                        )

                    numero_telefono = st.text_input(
                        "Telefono",
                        value=selected_record["telefono"],
                        key="telefono",
                        )
                        
                    monto_mensual = st.text_input(
                        "Monto mensual",
                        value=selected_record["monto_mensual"],
                        key="monto_mensual",
                        )
                        
                    if not monto_mensual.replace('.', '', 1).isdigit():
                        st.error("El monto mensual debe ser un número.")
                    else:
                        monto_mensual = float(monto_mensual)
                    
                with col2:
                    edad = st.text_input(
                        "Edad",
                        value=selected_record["edad"],
                        key="edad",
                        )

                    correo_electronico = st.text_input(
                        "Correo electronico ",
                        value=selected_record["correo_electronico"],
                        key="correo_electronico",
                        )
                        
                    monto_mensual_extra = st.text_input(
                        "Monto mensual extra",
                        value=selected_record["monto_mensual_extra"],
                        key="monto_mensual_extra",
                        )
                        
                    if not monto_mensual_extra.replace('.', '', 1).isdigit():
                        st.error("El monto mensual extra debe ser un número.")
                    else:
                        monto_mensual_extra = float(monto_mensual_extra)

                    if st.button("Guardar Cambios", key="save_button"):
                        
                        df_mi_perfil.at[selected_index, "nombre_user"] = nombre_user
                        df_mi_perfil.at[selected_index, "edad"] = edad
                        df_mi_perfil.at[selected_index, "telefono"] = numero_telefono
                        df_mi_perfil.at[selected_index, "correo_electronico"] = correo_electronico
                        df_mi_perfil.at[selected_index, "monto_mensual"] = monto_mensual
                            
                        df_mi_perfil.at[selected_index, "monto_mensual_extra"] = monto_mensual_extra

                        df_mi_perfil.to_csv(
                            "/usr/src/app/app/classes/logics/data/mi_perfil.csv",
                            mode="w",
                            index=False,
                        )

                        st.success("Perfil modificado exitosamente.")
                        time.sleep(2)
                        st.experimental_rerun()
        else:
            st.error("No hay datos disponibles para modificar.")
