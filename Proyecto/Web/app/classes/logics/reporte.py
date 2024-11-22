import streamlit as st
import pandas as pd
import time
from datetime import datetime

class Reporte:

    def logic(self) -> None:
        if not df_gastos_fijos.empty:

            df_gastos_fijos = pd.read_csv("/usr/src/app/app/classes/logics/data/Controldegastos/data_gastos_fijos.csv")

            df_gastos_fijos["Gasto mensual"] = pd.to_numeric(df_gastos_fijos["Gasto mensual"], errors='coerce')

            total_gastos_fijos = df_gastos_fijos["Gasto mensual"].sum()

            st.write(f"El total de los gastos fijos es: {total_gastos_fijos}")
        else:
            st.error("No existen datos disponibles para descargar el reporte.")
  
