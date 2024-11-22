import streamlit as st
import pandas as pd
import time
from datetime import datetime


class Gestor_gastos_fijos:
 
    def __init__(self) -> None:
        pass

    def logic(self) -> None:
        try:
            df_gastos_fijos = pd.read_csv("/usr/src/app/app/classes/logics/data/Controldegastos/data_gastos_fijos.csv")
            st.subheader("Gastos Fijos")
            st.dataframe(df_gastos_fijos)
            st.markdown("<br>", unsafe_allow_html=True)
            st.divider()
            st.markdown("<br>", unsafe_allow_html=True)
            if df_gastos_fijos.empty:
                self._add_gastos(df_gastos_fijos)
            else:
                tab_mostrar_gastos,tab_agregar_gastos ,tab_modificacion_gastos = st.tabs(["Mis Gastos","Agregar Gasto" ,"Modificación de Gastos"])
                with tab_mostrar_gastos:
                    self._displey_gastos(df_gastos_fijos)
                with tab_agregar_gastos:
                    self._add_gastos(df_gastos_fijos)
                with tab_modificacion_gastos:
                    self._modify_gastos(df_gastos_fijos)
                    
        except FileNotFoundError:
            st.error("Archivo CSV no encontrado. Por favor, verifíca la ruta.")
            df_gastos_fijos = pd.DataFrame(
                columns=[
                    "Categoria",
                    "Servicio",
                    "Descripcion",
                    "Gasto mensual",
                ]
            )
            st.dataframe(df_gastos_fijos)

    def _add_gastos(self, df_gastos_fijos:dict) -> None:
        tipo_categoria = st.selectbox(
            "Categoría",
            ("Vivienda", "Salud","Alimentos","Entretenimiento","Transporte"),
        )
        servicios = {
            "Vivienda": ["Alquiler", "Luz", "Agua", "Gas", "Internet"],
            "Salud": ["Seguro médico", "Medicamentos", "Gimnasio", "Terapia"],
            "Alimentos": ["Comida", "Bebidas", "Productos frescos"],
            "Entretenimiento": ["Netflix", "Spotify", "Amazon Prime", "Disney +", "YouTube", "Entretenimiento general"],
            "Transporte": ["Gasolina", "Transporte público", "Seguro vehícular"],
        }
        tipo_servicio = st.selectbox("Servicio", servicios[tipo_categoria])
        detalles_del_servicio = {
            "Alquiler": "Costo de vivienda",
            "Luz": "Energía eléctrica",
            "Agua": "Suministro de agua",
            "Gas": "Suministro de gas doméstico",
            "Internet": "Conexión a internet",
            "Seguro médico": "Plan de seguro de salud",
            "Medicamentos": "Gastos en medicinas",
            "Gimnasio": "Suscripción mensual al gimnasio",
            "Comida": "Compras de alimentos para el hogar",
            "Bebidas": "Consumo de bebidas en general",
            "Productos frescos": "Frutas, verduras y carnes",
            "Comida rápida": "Gastos en cadenas de comida",
            "Netflix": "Suscripción mensual de streaming",
            "Spotify": "Suscripción mensual de música",
            "Amazon Prime": "Suscripción mensual para streaming y envíos",
            "Entretenimiento general": "Gastos en ocio y actividades recreativas",
            "Gasolina": "Costo del combustible",
            "Transporte público": "Gastos para transportarse",
            "Mantenimiento del vehículo": "Reparaciones y servicios"
        }
        descripcion = detalles_del_servicio[tipo_servicio]
        gasto_mensual = st.text_input("Gasto mensual")
        st.write("")
        if st.button("Agregar Gasto"):
            if not str(gasto_mensual).replace('.', '', 1).isdigit() or float(gasto_mensual) < 0:
                st.error("El gasto mensual debe ser un número positivo.")
            else:
                new_record = {
                    "Categoria": tipo_categoria,
                    "Servicio": tipo_servicio ,
                    "Descripcion": descripcion,
                    "Gasto mensual": float(gasto_mensual),
                }
                df_gastos_fijos = df_gastos_fijos.append(new_record, ignore_index=True)
                df_gastos_fijos.to_csv("/usr/src/app/app/classes/logics/data/Controldegastos/data_gastos_fijos.csv", mode="w", index=False)
                st.success("Gasto agregado exitosamente.")
                time.sleep(3)
                st.experimental_rerun()

    def _displey_gastos(self, df_gastos_fijos:dict) -> None:
        st.markdown(
            """
            <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css" rel="stylesheet">
            """,
            unsafe_allow_html=True
        )
        for index, fila in df_gastos_fijos.iterrows():
            n_gasto = index + 1
            tipo_categoria = fila['Categoria']
            tipo_servicio = fila['Servicio']
            descripcion = fila['Descripcion']
            gasto_mensual = fila['Gasto mensual']
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
                    <p style='color: white;'> Gasto Mensual: {gasto_mensual}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.write("")

    def _modify_gastos(self, df_gastos_fijos:dict) -> None:
        st.subheader("Modificar Gastos Fijos Existentes")
        if not df_gastos_fijos.empty:
            opciones = list(range(1, len(df_gastos_fijos) + 1))
            selected_usuario = st.selectbox(
                "Selecciona el número del gasto a modificar", opciones
            )
            selected_index = selected_usuario - 1
            if selected_index is not None:
                selected_record = df_gastos_fijos.loc[selected_index]
                st.write("Categoría")
                tipo_categoria = selected_record['Categoria']
                st.markdown(
                    f"""
                    <div style="
                        border: 2px solid white; 
                        border-radius: 10px; 
                        padding: 2px; 
                        background-color: #151516;">
                        <p style='color: white; margin: 8px;'> {tipo_categoria}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                st.write("")
                st.write("Servicio")
                tipo_servicio = selected_record['Servicio']
                st.markdown(
                    f"""
                    <div style="
                        border: 2px solid white; 
                        border-radius: 10px; 
                        padding: 2px; 
                        background-color: #151516;">
                        <p style='color: white; margin: 8px;'> {tipo_servicio}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                st.write("")
                descripcion = st.text_input(
                    "Descripción",
                    value=selected_record["Descripcion"],
                    key=",Descripcion",
                )
                gasto_mensual = st.text_input(
                    "Gasto mensual",
                    value=selected_record["Gasto mensual"],
                    key=",Gasto mensual",
                )
                st.write("")
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Guardar Cambios", key="save_button"):
                        df_gastos_fijos.at[selected_index, "Descripcion"] = descripcion
                        if not str(gasto_mensual).replace('.', '', 1).isdigit() or float(gasto_mensual) < 0:
                            st.error("El gasto mensual debe ser un número positivo.")
                        else:
                            df_gastos_fijos.at[selected_index, "Gasto mensual"] = float(gasto_mensual)
                            df_gastos_fijos.to_csv(
                                "/usr/src/app/app/classes/logics/data/Controldegastos/data_gastos_fijos.csv",
                                mode="w",
                                index=False,
                            )
                        st.success("Gasto modificado exitosamente.")
                        time.sleep(3) 
                        st.experimental_rerun() 
                st.write("")
                with col2:
                    if st.button("Eliminar Gasto", key="save_button2"):
                        csv_file = '/usr/src/app/app/classes/logics/data/Controldegastos/data_gastos_fijos.csv'
                        df_gastos_fijos = df_gastos_fijos.drop(index=selected_index)
                        df_gastos_fijos = df_gastos_fijos.reset_index(drop=True)
                        df_gastos_fijos.to_csv(csv_file, index=False)
                        st.success("Gasto eliminado exitosamente.")
                        time.sleep(3) 
                        st.experimental_rerun()
        else:
            st.error("No existen gastos disponibles para modificar.")
