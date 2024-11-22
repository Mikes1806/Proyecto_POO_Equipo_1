import streamlit as st
import pandas as pd
import time
from datetime import datetime


class Gestor_gastos_imprevistos:
 
    def __init__(self) -> None:
        pass

    def logic(self) -> None:
        try:
            df_gastos_imprevistos = pd.read_csv("/usr/src/app/app/classes/logics/data/Controldegastos/data_gastos_imprevistos.csv")
            st.subheader("Gastos Imprevistos")
            st.dataframe(df_gastos_imprevistos)
            st.markdown("<br>", unsafe_allow_html=True)
            st.divider()
            st.markdown("<br>", unsafe_allow_html=True)
            if df_gastos_imprevistos.empty:
                self._add_gastos(df_gastos_imprevistos)
            else:
                tab_mostrar_gastos,tab_agregar_gastos ,tab_modificacion_gastos = st.tabs(["Mis Gastos","Agregar Gasto" ,"Modificación de Gastos"])
                with tab_mostrar_gastos:
                    self._displey_gastos(df_gastos_imprevistos)
                with tab_agregar_gastos:
                    self._add_gastos(df_gastos_imprevistos)
                with tab_modificacion_gastos:
                    self._modify_gastos(df_gastos_imprevistos)
                    
        except FileNotFoundError:
            st.error("Archivo CSV no encontrado. Por favor, verifíca la ruta.")
            df_gastos_imprevistos = pd.DataFrame(
                columns=[
                    "Categoria",
                    "Servicio",
                    "Descripcion",
                    "Costo",
                ]
            )
            st.dataframe(df_gastos_imprevistos)

    def _add_gastos(self, df_gastos_imprevistos:dict) -> None:
        tipo_categoria = st.selectbox(
            "Categoría",
            ("Vivienda", "Salud","Alimentos","Entretenimiento","Transporte"),
        )
        servicios = {
            "Vivienda": ["Reparaciones", "Mudanza"],
            "Salud": ["Medicamentos", "Emergencia médica", "Emergencia quirúrgica"],
            "Alimentos": ["Comida", "Bebidas", "Comida rápida"],
            "Entretenimiento": ["Juegos", "Entradas para eventos", "Música"],
            "Transporte": ["Mantenimiento del vehículo", "Tramite vehicular", "Movilidad por aplicación"],
        }
        tipo_servicio = st.selectbox("Servicio", servicios[tipo_categoria])
        descripcion = st.text_input("Descripcion (Opcional)")
        costo = st.text_input("Costo")
        st.write("")
        if st.button("Agregar Gasto"):
            if not str(costo).replace('.', '', 1).isdigit() or float(costo) < 0:
                st.error("El costo debe ser un número positivo.")
            else:
                new_record = {
                    "Categoria": tipo_categoria,
                    "Servicio": tipo_servicio ,
                    "Descripcion": descripcion,
                    "Costo": float(costo),
                }
                df_gastos_imprevistos = df_gastos_imprevistos.append(new_record, ignore_index=True)
                df_gastos_imprevistos.to_csv("/usr/src/app/app/classes/logics/data/Controldegastos/data_gastos_imprevistos.csv", mode="w", index=False)
                st.success("Gasto agregado exitosamente.")
                time.sleep(3)
                st.experimental_rerun()

    def _displey_gastos(self, df_gastos_imprevistos:dict) -> None:
        st.markdown(
            """
            <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css" rel="stylesheet">
            """,
            unsafe_allow_html=True
        )
        for index, fila in df_gastos_imprevistos.iterrows():
            n_gasto = index + 1
            tipo_categoria = fila['Categoria']
            tipo_servicio = fila['Servicio']
            descripcion = fila['Descripcion']
            costo = fila['Costo']
            iconos_servicio = {
            "Vivienda": "house-heart",
            "Salud": "heart-pulse",
            "Alimentos": "basket-fill",
            "Entretenimiento": "emoji-laughing",
            "Transporte": "truck-front-fill",
            }
            icono_gasto = iconos_servicio.get(tipo_categoria)
            st.subheader(f"Gasto de {tipo_categoria}")
            st.markdown(
                f"""
                <div style="
                    border: 2px solid white; 
                    border-radius: 10px; 
                    padding: 10px; 
                    background-color: #151516;
                    width: 100%; 
                    max-width: 800px; 
                    margin: auto;">
                    <p style='color: white;'> 
                    <i class="bi bi-{icono_gasto}" style="margin-right: 8px;"></i></p>
                    <p style='color: white;'> Número de Gasto: {n_gasto}</p>
                    <p style='color: white;'> Servicio: {tipo_servicio}</p>
                    <p style='color: white;'> Descripción: {descripcion}</p>
                    <p style='color: white;'> Costo: {costo}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.write("")

    def _modify_gastos(self, df_gastos_imprevistos:dict) -> None:
        st.subheader("Modificar Gastos Imprevistos Existentes")
        if not df_gastos_imprevistos.empty:
            opciones = list(range(1, len(df_gastos_imprevistos) + 1))
            selected_usuario = st.selectbox(
                "Selecciona el número del gasto a modificar", opciones
            )
            selected_index = selected_usuario - 1
            if selected_index is not None:
                selected_record = df_gastos_imprevistos.loc[selected_index]
                tipo_categoria = st.selectbox(
                    "Categoría",
                    ["Vivienda", "Salud", "Alimentos", "Entretenimiento", "Transporte"],
                    index=["Vivienda", "Salud", "Alimentos", "Entretenimiento", "Transporte"].index(selected_record["Categoria"]),
                    key="Categoria",
                )
                st.write("")
                tipo_servicio = st.text_input(
                    "Servicio",
                    value=selected_record["Servicio"],
                    key=",Servicio",
                )
                st.write("")
                descripcion = st.text_input(
                    "Descripción",
                    value=selected_record["Descripcion"],
                    key=",Descripcion",
                )
                costo = st.text_input(
                    "Costo",
                    value=selected_record["Costo"],
                    key=",Costo",
                )
                st.write("")
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Guardar Cambios", key="save_button"):
                        df_gastos_imprevistos.at[selected_index, "Categoria"] = tipo_categoria
                        df_gastos_imprevistos.at[selected_index, "Servicio"] = tipo_servicio
                        df_gastos_imprevistos.at[selected_index, "Descripcion"] = descripcion
                        if not str(costo).replace('.', '', 1).isdigit() or float(costo) < 0:
                            st.error("El costo debe ser un número positivo.")
                        else:
                            df_gastos_imprevistos.at[selected_index, "Costo"] = float(costo)
                            df_gastos_imprevistos.to_csv(
                                "/usr/src/app/app/classes/logics/data/Controldegastos/data_gastos_imprevistos.csv",
                                mode="w",
                                index=False,
                            )
                        st.success("Gasto modificado exitosamente.")
                        time.sleep(3) 
                        st.experimental_rerun() 
                st.write("")
                with col2:
                    if st.button("Eliminar Gasto", key="save_button2"):
                        csv_file = '/usr/src/app/app/classes/logics/data/Controldegastos/data_gastos_imprevistos.csv'
                        df_gastos_imprevistos = df_gastos_imprevistos.drop(index=selected_index)
                        df_gastos_imprevistos = df_gastos_imprevistos.reset_index(drop=True)
                        df_gastos_imprevistos.to_csv(csv_file, index=False)
                        st.success("Gasto eliminado exitosamente.")
                        time.sleep(3) 
                        st.experimental_rerun()
        else:
            st.error("No existen gastos disponibles para modificar.")
