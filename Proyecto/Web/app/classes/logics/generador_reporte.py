import streamlit as st
import pandas as pd
import time
from datetime import datetime

class Gestor_generador_reporte:
    def __init__(self) -> None:
        pass

    def logic(self) -> None:
        # Cargar los datos desde cada archivo CSV
        ruta_necesidades = '/usr/src/app/app/classes/logics/data/Controldegastos/data_gastos_fijos.csv'
        ruta_deseos = '/usr/src/app/app/classes/logics/data/Controldegastos/data_gastos_imprevistos.csv'
        ruta_ahorros = '/usr/src/app/app/classes/logics/data/mi_perfil.csv'

        # Leer los archivos CSV
        df_necesidades = pd.read_csv(ruta_necesidades)
        df_deseos = pd.read_csv(ruta_deseos)
        df_ahorros = pd.read_csv(ruta_ahorros)

        # Calcular la suma total de gastos para cada categoría
        suma_necesidades = df_necesidades['Gasto mensual'].sum()
        suma_deseos = df_deseos['Gasto mensual'].sum()
        suma_ahorros = df_ahorros['monto_mensual'].sum()

        # Calcular el total de ingresos netos (sumando todas las categorías)
        ingresos_brutos = suma_necesidades + suma_deseos + suma_ahorros
        ingresos_netos = ingresos_brutos - (suma_necesidades + suma_deseos)

        # Calcular los porcentajes recomendados
        necesidades_recomendadas = 0.5 * ingresos_netos
        deseos_recomendados = 0.3 * ingresos_netos
        ahorros_recomendados = 0.2 * ingresos_netos

        # Configurar la interfaz Streamlit
        st.title("Balance de Gastos: Regla del 50/30/20")
        st.subheader("Total Ingresos y Gastos")

        # Mostrar total de ingresos y gastos por categoría
        st.subheader("Ingresos 50+30+20 = 100%")
        st.write(f"**Total de Ingresos Netos**: ${ingresos_brutos}")
        st.subheader("Gastos en Necesidades 50%")
        st.write(f"**Gastos en Necesidades**: ${suma_necesidades} ")
        st.write(f"**Recomendado en Necesidades:** ${necesidades_recomendadas}")
        st.subheader("Gastos en Deseos 30%")
        st.write(f"**Gastos en Deseos**: ${suma_deseos}")
        st.write(f"**Recomendado en Deseos:** ${deseos_recomendados}")
        st.subheader("Ahorro o Inversión 20%")
        st.write(f"**Dinero destinable al Ahorro**: ${ingresos_netos}")
        st.write(f"**Recomendado en Ahorro:** ${ahorros_recomendados}")

        # Verificar si se cumple con la regla 50/30/20
        cumple_necesidades = suma_necesidades <= necesidades_recomendadas
        cumple_deseos = suma_deseos <= deseos_recomendados
        cumple_ahorros = suma_ahorros >= ahorros_recomendados

        # Mostrar verificación
        st.subheader("Verificación de la Regla 50/30/20")
        st.write(f"¿Cumple con el 50% en Necesidades?: {'¡Sí, vas por buen Camino!' if cumple_necesidades else 'No, recuerda tus Prioridades'}")
        st.write(f"¿Cumple con el 30% en Deseos?: {'¡Sí, vas por buen Camino!' if cumple_deseos else 'No, recuerda tus Prioridades'}")
        st.write(f"¿Cumple con el 20% en Ahorros?: {'¡Sí, vas por buen Camino!' if cumple_ahorros else 'No, recuerda tus Prioridades'}")

        # Crear un DataFrame con la información que quieres exportar
        data = {
            'Categoria': ['Necesidades', 'Deseos', 'Ahorros'],
            'Gasto Total': [suma_necesidades, suma_deseos, suma_ahorros],
            'Recomendado': [necesidades_recomendadas, deseos_recomendados, ahorros_recomendados],
            'Cumple con la Regla': [
                'Si' if cumple_necesidades else 'No',
                'Si' if cumple_deseos else 'No',
                'Si' if cumple_ahorros else 'No'
            ]
        }
        
        df_balance = pd.DataFrame(data)

        # Descargar el archivo CSV
        st.title("Presiona aquí para descargar tu balance")
        st.download_button(
            label="Descargar Balance como CSV",
            data=df_balance.to_csv(index=False).encode('utf-8'),
            file_name='balance_gastos.csv',
            mime='text/csv'
        )