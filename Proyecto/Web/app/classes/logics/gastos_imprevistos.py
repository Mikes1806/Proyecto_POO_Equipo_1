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
            #st.subheader("Gastos imprevistos")
            #st.dataframe(df_gastos_imprevistos)
            #st.markdown("<br>", unsafe_allow_html=True)
            #st.divider()
            #st.markdown("<br>", unsafe_allow_html=True)
            if df_gastos_imprevistos.empty:
                self._add_gastos(df_gastos_imprevistos)
            else:
                tab_mostrar_gastos,tab_agregar_gastos ,tab_modificacion_gastos = st.tabs(["Mi información","Agregar nuevo gasto" ,"Modificación de información"])
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
                    "Gasto mensual",
                    "Descripción",
                    "Comentario",
                ]
            )
            st.dataframe(df_gastos_imprevistos)

    def _add_gastos(self, df_gastos_imprevistos):
        tipo_categoria = st.selectbox(
        "Categoria",
        ("Vivienda", "Salud","Alimentos","Entretenimiento","Transporte"),
        )
        servicios = {
            "Vivienda": ["Alquiler", "Luz", "Agua", "Gas", "Internet"],
            "Salud": ["Seguro medico", "Medicamentos", "Agua", "Gimnasio"],
            "Alimentos": ["Comida", "Bebidas", "Productos frescos", "Comida rapida"],
            "Entretenimiento": ["Netflix", "Spotify", "Amazon Prime", "Disney +", "Entretenimiento general"],
            "Transporte": ["Gasolina", "Transporte público", "Mantenimiento del vehículo"],
        }
        tipo_servicio = st.selectbox("Servicio", servicios[tipo_categoria])
        gasto_mensual = st.text_input("Gasto mensual")
        detalles_del_servicio = {
            "Alquiler": "Costo de vivienda",
            "Luz": "Energía eléctrica",
            "Agua": "Suministro de agua potable",
            "Gas": "Suministro de gas doméstico",
            "Internet": "Conexión a internet",
            "Seguro medico": "Plan de seguro de salud",
            "Medicamentos": "Gastos en medicinas",
            "Gimnasio": "Suscripción mensual al gimnasio",
            "Comida": "Compras de alimentos para el hogar",
            "Bebidas": "Consumo de bebidas en general",
            "Productos frescos": "Frutas, verduras y carnes",
            "Comida rapida": "Gastos en cadenas de comida",
            "Netflix": "Suscripción mensual de streaming",
            "Spotify": "Suscripción mensual de música",
            "Amazon Prime": "Suscripción mensual para streaming y envíos",
            "Entretenimiento general": "Gastos en ocio y actividades recreativas",
            "Gasolina": "Costo del combustible",
            "Transporte público": "Gastos en autobuses o trenes",
            "Mantenimiento del vehículo": "Reparaciones y servicios"
        }
        descripcion = detalles_del_servicio[tipo_servicio]
        comentario = st.text_input("Comentario (opcional)")
        if st.button("Agregar Gasto"):
            new_record = {
                "Categoria": tipo_categoria,
                "Servicio": tipo_servicio ,
                "Gasto mensual": gasto_mensual,
                "Descripción": descripcion,
                "Comentario": comentario,
            }
            df_gastos_imprevistos = df_gastos_imprevistos.append(new_record, ignore_index=True)
            df_gastos_imprevistos.to_csv("/usr/src/app/app/classes/logics/data/Controldegastos/data_gastos_imprevistos.csv", mode="w", index=False)
            st.success("Gasto agregado exitosamente.")
            time.sleep(3)
            st.experimental_rerun()

    def _displey_gastos(self, df_gastos_imprevistos):
        st.markdown(
            """
            <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css" rel="stylesheet">
            """,
            unsafe_allow_html=True
        )
        for index, fila in df_gastos_imprevistos.iterrows():
            tipo_categoria = fila['Categoria']
            tipo_servicio = fila['Servicio']
            gasto_mensual = fila['Gasto mensual']
            descripcion = fila['Descripción']
            comentario = fila['Comentario']
            iconos_servicio = {
            "Vivienda": "house-heart",
            "Salud": "heart-pulse",
            "Alimentos": "basket-fill",
            "Entretenimiento": "emoji-laughing",
            "Transporte": "truck-front-fill",
            }

            icono_gasto = iconos_servicio.get(tipo_categoria)

            st.write(f"Gasto para: {tipo_categoria}")
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
                <p style='color: white;'> Servicio: {tipo_servicio}</p>
                <p style='color: white;'> Gasto mensual: {gasto_mensual}</p>
                <p style='color: white;'> Descripcion: {descripcion}</p>
                <p style='color: white;'> Comentario: {comentario}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.write("") 
            st.write("") 

    def _modify_gastos(self, df_gastos_imprevistos):
        #st.subheader("Modificar Gastos Existentes")
        if not df_gastos_imprevistos.empty:
            selected_servicio = st.selectbox(
                "Selecciona un contacto para modificar",
                df_gastos_imprevistos['Servicio'],
            )
            if selected_servicio is not None:
                st.write(f" {selected_servicio}") 
                selected_record = df_gastos_imprevistos[df_gastos_imprevistos['Servicio'] == selected_servicio].iloc[0]
                tipo_categoria = selected_record['Categoria']
                tipo_servicio = selected_record['Servicio']
                gasto_mensual = st.text_input(
                    "Gasto mensual",
                    value=selected_record["Gasto mensual"],
                    key=",Gasto mensual",
                )
                descripcion = st.text_input(
                    "Descripción",
                    value=selected_record["Descripción"],
                    key=",Descripcion",
                )
                comentario = st.text_input(
                    "Comentario",
                    value=selected_record["Comentario"],
                    key=",Comentario",
                )
                st.write("") 
                st.write("") 
                if st.button("Guardar Cambios", key="save_button"):
                    df_gastos_imprevistos.loc[df_gastos_imprevistos['Servicio'] == selected_servicio, 'Categoria'] = tipo_categoria
                    df_gastos_imprevistos.loc[df_gastos_imprevistos['Servicio'] == selected_servicio, 'Servicio'] = tipo_servicio
                    df_gastos_imprevistos.loc[df_gastos_imprevistos['Servicio'] == selected_servicio, 'Gasto mensual'] = gasto_mensual
                    df_gastos_imprevistos.loc[df_gastos_imprevistos['Servicio'] == selected_servicio, 'Descripción'] = descripcion
                    df_gastos_imprevistos.loc[df_gastos_imprevistos['Servicio'] == selected_servicio, 'Comentario'] = comentario
                    df_gastos_imprevistos.to_csv(
                        "/usr/src/app/app/classes/logics/data/Controldegastos/data_gastos_imprevistos.csv",
                        mode="w",
                        index=False,
                    )
                    st.success("Registro modificado exitosamente.")
                    time.sleep(2)
                    st.experimental_rerun()
                    st.write("") 
                    st.write("")
                    if st.button("Eliminar gasto", key="save_button2"):
                        csv_file = '/usr/src/app/app/classes/logics/data/Controldegastos/data_gastos_imprevistos.csv'
                        df_gastos_imprevistos = df_gastos_imprevistos[df_gastos_imprevistos['Servicio'] != selected_servicio] 
                        df_gastos_imprevistos.to_csv(csv_file, index=False)  
                        st.success("Gasto eliminado exitosamente.")
                        time.sleep(3)
                        st.experimental_rerun()
        else:
            st.error("No hay registros disponibles para modificar.")
