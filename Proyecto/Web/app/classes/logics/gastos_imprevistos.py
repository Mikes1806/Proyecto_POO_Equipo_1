import streamlit as st
import pandas as pd
import time
from datetime import datetime

df_gastos_fijos = pd.read_csv(
    "/usr/src/app/app/classes/logics/data/Controldegastos/data_muestra.csv"
)

print(df_gastos_fijos)

