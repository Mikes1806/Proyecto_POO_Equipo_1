import streamlit as st
import pandas as pd
import time
from datetime import datetime

class Gestor_gastos_fijos:
 def __init__(self) -> None:

    pass

 def logic(self):

        try:

            df_gastos_fijos = pd.read_csv(
                "/usr/src/app/app/classes/logics/data/Controldegastos/data_gastos_fijos.csv"
            )
            st.subheader("Gastos fijos")
            st.dataframe(df_gastos_fijos)
            st.markdown("<br>", unsafe_allow_html=True)
            st.divider()
            st.markdown("<br>", unsafe_allow_html=True)

            if df_gastos_fijos.empty:
                self._add_Gastos(df_gastos_fijos)

                


            else:
              tab_mostrar_gastos, tab_modificacion_gastos = st.tabs(["Mi informacion", "Modificacion de informacion"])

              with tab_mostrar_gastos:
                self._displey_gatos(df_gastos_fijos)
              with tab_modificacion_gastos:
                self._modify_gastos(df_gastos_fijos)

        except FileNotFoundError:
            st.error("Archivo CSV no encontrado. Por favor, verifica la ruta.")
            df_gastos_fijos = pd.DataFrame(
                columns=[
                    "Categoria",
                    "Servicio",
                    "Gasto mensual",
                    "Descripcion",
                    "Comentario",
                ]
            )
            st.dataframe(df_gastos_fijos)


 def _add_Gastos(self, df_gastos_fijos):

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
                "Descripcion": descripcion,
                "Comentario": comentario,
            }

            df_gastos_fijos = df_gastos_fijos.append(new_record, ignore_index=True)
            df_gastos_fijos.to_csv(
                 "/usr/src/app/app/classes/logics/data/Controldegastos/data_gastos_fijos.csv",
                mode="w",
                index=False,
                )
            st.success("Registro agregado exitosamente.")
            time.sleep(5)
            st.experimental_rerun()

 def _displey_gatos(df_gastos_fijos):
     pass
 
 def _modify_gastos(df_gastos_fijos):
     pass
