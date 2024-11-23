import streamlit as st
import pandas as pd
import time
from datetime import datetime


class Reporte:

    def logic(self) -> None:
        df_mi_perfil = pd.read_csv("/usr/src/app/app/classes/logics/data/mi_perfil.csv")
        df_gastos_fijos = pd.read_csv("/usr/src/app/app/classes/logics/data/Controldegastos/data_gastos_fijos.csv")
        df_gastos_imprevistos = pd.read_csv("/usr/src/app/app/classes/logics/data/Controldegastos/data_gastos_imprevistos.csv")
        if not df_mi_perfil.empty or not df_gastos_fijos.empty or not df_gastos_imprevistos.empty:
            df_mi_perfil["monto_mensual_total"] = pd.to_numeric(df_mi_perfil["monto_mensual_total"], errors='coerce')
            df_gastos_fijos["Gasto mensual"] = pd.to_numeric(df_gastos_fijos["Gasto mensual"], errors='coerce')
            df_gastos_imprevistos["Costo"] = pd.to_numeric(df_gastos_imprevistos["Costo"], errors='coerce')
            total_monto_mensual = df_mi_perfil["monto_mensual_total"]
            total_gastos_fijos = df_gastos_fijos["Gasto mensual"].sum()
            total_gastos_imprevistos = df_gastos_imprevistos["Costo"].sum()
            disponibilidad = float(total_monto_mensual) - (float(total_gastos_fijos) + float(total_gastos_imprevistos))
            self._display_report(df_gastos_fijos,df_gastos_imprevistos,total_monto_mensual,total_gastos_fijos,total_gastos_imprevistos,disponibilidad)
        else:
            st.error("No existen datos suficientes para generar un reporte.")

    def _display_report(self, df_gastos_fijos:dict, df_gastos_imprevistos:dict, total_monto_mensual:float, total_gastos_fijos:float, total_gastos_imprevistos:float, disponibilidad:float) -> None:
            st.subheader(f"Gastos Fijos")
            st.markdown(
                f"""
                <div style="
                    border: 2px solid white; 
                    border-radius: 7px; 
                    padding: 10px; 
                    background-color: #151516;
                    width: 100%; 
                    max-width: 800px; 
                    margin: auto;
                    text-align: center;">
                    <p style='color: white; margin: 5px;'>
                        <b>Total de gastos fijos:</b> ${float(total_gastos_fijos):.2f}
                    </p>
                    <p style='color: white; margin: 5px;'>
                        <b>Porcentaje sobre el ingreso mensual:</b> {float(total_gastos_fijos)/float(total_monto_mensual)*100:.2f}%
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.write("")
            st.write("")
            if st.download_button(
                label = "Descargar Reporte",
                data = df_gastos_fijos.to_csv(index=False).encode('utf-8'),
                file_name = 'Mis_Gastos_Fijos.csv',
                mime = 'text/csv'
                ):
                with st.spinner("Descargando..."):
                    time.sleep(3) 
                st.success("Reporte Descargado.")
                time.sleep(3)
                st.experimental_rerun()
            st.subheader(f"Gastos Imprevistos")
            st.markdown(
                f"""
                <div style="
                    border: 2px solid white; 
                    border-radius: 7px; 
                    padding: 10px; 
                    background-color: #151516;
                    width: 100%; 
                    max-width: 800px; 
                    margin: auto;
                    text-align: center;">
                    <p style='color: white; margin: 5px;'>
                        <b>Total de gastos imprevistos:</b> ${float(total_gastos_imprevistos):.2f}
                    </p>
                    <p style='color: white; margin: 5px;'>
                        <b>Porcentaje sobre el ingreso mensual:</b> {float(total_gastos_imprevistos)/float(total_monto_mensual)*100:.2f}%
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.write("")
            st.write("")
            if st.download_button(
                label = "Descargar Reporte",
                data = df_gastos_imprevistos.to_csv(index=False).encode('utf-8'),
                file_name = 'Mis_Gastos_Imprevistos.csv',
                mime = 'text/csv'
                ):
                with st.spinner("Descargando..."):
                    time.sleep(3) 
                st.success("Reporte Descargado.")
                time.sleep(3)
                st.experimental_rerun()
            st.subheader(f"Monto Disponible")
            st.markdown(
                f"""
                <div style="
                    border: 2px solid white; 
                    border-radius: 7px; 
                    padding: 10px; 
                    background-color: #151516;
                    width: 100%; 
                    max-width: 800px; 
                    margin: auto;
                    text-align: center;">
                    <p style='color: white; margin: 5px;'>
                        <b>Monto mensual disponible:</b> ${float(disponibilidad):.2f}
                    </p>
                    <p style='color: white; margin: 5px;'>
                        <b>Porcentaje restante:</b> {float(disponibilidad)/float(total_monto_mensual)*100:.2f}%
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
  