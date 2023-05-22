import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

st.title("Índice de supervivencia")
st.markdown("**Descripción**")
st.write("Porcentaje de personas que sobreviven a los accidentes aéreos respecto al total de personas involucradas")
st.markdown("**Fórmula de medición**")
st.write("(Total_Sobrevivientes / Total_Personas_Involucradas) * 100")
st.markdown("**KPI**")
st.write("Aumentar el índice de supervivencia en un 5% anualmente.")

# Cargar dataframe con las columnas necesarias
columnas = ["Año", "Total_Fallecidos", "Total_A_bordo", "Muertos_en_tierra", "resumen"]
df_accidentes = pd.read_csv("df_accidente3.csv", sep=",", usecols=columnas)
df_accidentes.dropna(inplace=True)

#Creamos columna Sobrevivientes
df_accidentes["Sobrevivientes"] = df_accidentes["Total_A_bordo"] - df_accidentes["Total_Fallecidos"]

#Creamos tasa de sobrevivientes
df_accidentes["Tasa_Sobrevivientes"] = df_accidentes["Sobrevivientes"]/df_accidentes["Total_A_bordo"]

# Convertir la columna "Año" a tipo entero
df_accidentes['Año'] = df_accidentes['Año'].astype(int)

# Reordenar las columnas
columnas_reordenadas = ["Año","Tasa_Sobrevivientes", "Sobrevivientes", "Total_Fallecidos", "Muertos_en_tierra", "resumen"]
df_accidentes = df_accidentes[columnas_reordenadas]

if st.checkbox("Ver información de accidentes detallado en tabla"):
    st.dataframe(df_accidentes)




if st.checkbox("Gráfico de tendencia de sobrevivientes y fallecidos en la historia"):
    Año_minimo = st.slider("Definir año mínimo", 1920, 2021, 1920)
    Año_maximo = st.slider("Definir año máximo", 1920, 2021, 2021)

    # Filtrar los datos por rango de años
    datos_filtrados = df_accidentes[(df_accidentes['Año'] >= Año_minimo) & (df_accidentes['Año'] <= Año_maximo)]

    # Agrupar los datos por año y sumar los valores de "Sobrevivientes" y "Total_Fallecidos"
    datos_por_año = datos_filtrados.groupby('Año')[['Sobrevivientes', 'Total_Fallecidos']].sum()

    # Crear el gráfico de líneas
    fig, ax = plt.subplots()
    datos_por_año.plot(kind='line', ax=ax)

    # Configurar los ejes y el título
    ax.set_xlabel('Año')
    ax.set_ylabel('Cantidad')
    ax.set_title('Sobrevivientes y Fallecidos por año')

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)


