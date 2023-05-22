import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.ticker import MaxNLocator

st.title("Indice de Mejora de la seguridad")
st.markdown("**Descripción**")
st.write("Medida de la mejora en la seguridad aérea en términos de reducción en la tasa de mortalidad anual")
st.markdown("**Fórmula de medición**")
st.write("((Tasa_accidentalidad_Año_Anterior - Tasa_accidentalidad_Año_Actual) / Tasa_accidentalidad_Año_Anterior) * 100")
st.markdown("**KPI**")
st.write("Mejorar el índice de mejora de la seguridad en un 10% anualmente.")

# Cargar dataframe con las columnas necesarias
columnas = ["Año", "Tasa_Mortalidad", "Total_Fallecidos", "Total_A_bordo", "Muertos_en_tierra", "resumen"]
df_accidentes = pd.read_csv("df_accidente3.csv", sep=",", usecols=columnas)
df_accidentes.dropna(inplace=True)

# Reordenar las columnas
columnas_reordenadas = ["Año", "Tasa_Mortalidad", "Total_Fallecidos", "Total_A_bordo", "Muertos_en_tierra", "resumen"]
df_accidentes = df_accidentes[columnas_reordenadas]


if st.checkbox("Ver información detallada de los accidentes aéreos en la historia"):
    st.dataframe(df_accidentes)
    
#Tabla accidentalidad
if st.checkbox("Tabla resumen de la Tasa de accidentalidad año a año"):
    # Calcular la tasa de accidentalidad por año (conteo de registros por año)
    df_accidentes['Tasa_accidentalidad'] = df_accidentes.groupby('Año').size()

    # Ordenar el DataFrame por el año en orden ascendente
    df_accidentes = df_accidentes.sort_values('Año')

    # Calcular la disminución/aumento de la tasa de accidentalidad con respecto al año anterior y redondear los valores
    df_accidentes['Disminucion/Aumento'] = ((df_accidentes['Tasa_accidentalidad'].shift(1) - df_accidentes['Tasa_accidentalidad']) / df_accidentes['Tasa_accidentalidad'].shift(1)) * 100

    # Filtrar las columnas necesarias (Año y Disminucion/Aumento) y eliminar filas con valores NaN
    df_resultado = df_accidentes[['Año', 'Disminucion/Aumento']].dropna()

    # Tomar los top 20 resultados
    df_top_20 = df_resultado.head(20)

    # Mostrar la tabla resultante
    st.table(df_top_20)

#Grafico

import matplotlib.pyplot as plt
import streamlit as st

if st.checkbox("Ver gráfico de dispersión"):

    Año_minimo = st.slider("Definir año mínimo", 1920, 2021, 1920)
    Año_maximo = st.slider("Definir año máximo", 1920, 2021, 2021)
    
    # Filtrar los datos por el rango de años seleccionado
    df_filtrado = df_accidentes[(df_accidentes['Año'] >= Año_minimo) & (df_accidentes['Año'] <= Año_maximo)]
    
    # Obtener la frecuencia de accidentes por año en los datos filtrados
    frecuencia_por_año = df_filtrado['Año'].value_counts().reset_index()
    frecuencia_por_año.columns = ['Año', 'frecuencia']

    # Crear el gráfico de dispersión
    plt.scatter(frecuencia_por_año['Año'], frecuencia_por_año['frecuencia'])

    # Configurar los ejes y el título
    plt.xlabel('Año')
    plt.ylabel('Frecuencia de accidentes')
    plt.title('Frecuencia de accidentes por año')

    # Mostrar el gráfico en Streamlit
    st.pyplot()






