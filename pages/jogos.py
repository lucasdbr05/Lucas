import streamlit
import pandas as pd
import datetime
from datetime import date
import numpy as np


st.title("Jogos do Dia")

dia = st.date_input("Data de Análise" ,date.today())

def load_data_jogos():
  data_jogos = pd.read_csv(f"https://github.com/futpythontrader/YouTube/blob/main/Jogos_do_Dia_FlashScore/{str(dia)}_Jogos_do_Dia_FlashScore.csv?raw=True")
  return data_jogos


df_jogos = load_data_jogos()

st.dataframe(df_jogos)
