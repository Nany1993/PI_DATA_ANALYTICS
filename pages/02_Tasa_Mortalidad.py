import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

st.title("Tasa de Mortalidad Anual")
st.markdown("**Descripción**")
st.write("Porcentaje de fallecidos en los accidentes aéreos respecto al total de personas en los vuelos involucrados")
st.markdown("**Fórmula de medición**")
st.write("(Total_Fallecidos / Total_A_bordo) * 100  ")
st.markdown("**KPI**")
st.write("Reducir en un 5% la tasa de mortalidad anualmente")

# Cargar dataframe con las columnas necesarias
columnas = ["Año", "Tasa_Mortalidad", "Total_Fallecidos", "Total_A_bordo", "Muertos_en_tierra", "resumen"]
df_accidentes = pd.read_csv("df_accidente3.csv", sep=",", usecols=columnas)
df_accidentes.dropna(inplace=True)

# Convertir la columna "Año" a tipo entero
df_accidentes['Año'] = df_accidentes['Año'].astype(int)

# Reordenar las columnas
columnas_reordenadas = ["Año", "Tasa_Mortalidad", "Total_Fallecidos", "Total_A_bordo", "Muertos_en_tierra", "resumen"]
df_accidentes = df_accidentes[columnas_reordenadas]


if st.checkbox("Ver información de accidentes detallado en tabla"):
    st.dataframe(df_accidentes)


if st.checkbox("Tabla resumen con los años más impactados en la historia a nivel de mortalidad"):
    # Calcular la tasa de mortalidad
    
    df_accidentes["Tasa_Mortalidad"] = df_accidentes["Total_Fallecidos"] / df_accidentes["Total_A_bordo"] * 100

    # Reemplazar los valores infinitos con NaN
    df_accidentes.replace([np.inf, -np.inf], np.nan, inplace=True)

    # Eliminar filas con valores NaN en 'Año' y 'Tasa_Mortalidad'
    df_accidente2_cleaned = df_accidentes.dropna(subset=['Año', 'Tasa_Mortalidad'])
   

    # Filtrar las filas con valores no nulos en 'Tasa_Mortalidad'
    df_accidente2_cleaned = df_accidente2_cleaned[df_accidente2_cleaned['Tasa_Mortalidad'].notnull()]

    # Agrupar los datos limpios por año y calcular la cantidad de accidentes y la tasa de mortalidad promedio
    df_grouped = df_accidente2_cleaned.groupby('Año').agg({'Tasa_Mortalidad': 'mean', 'Año': 'size'}).rename(columns={'Año': 'Cantidad_Accidentes'})

    # Calcular la columna de incremento/reducción
    df_grouped['Incremento/Reducción'] = df_grouped['Cantidad_Accidentes'].diff()

    # Calcular la reducción porcentual de la tasa de mortalidad
    df_grouped['Reducción_Tasa'] = df_grouped['Tasa_Mortalidad'].pct_change()

    # Ordenar por cantidad de accidentes en orden descendente y tomar los primeros 20 resultados
    df_top_20 = df_grouped.sort_values('Cantidad_Accidentes', ascending=False).head(30)

    # Mostrar la tabla resultante
    st.table(df_top_20)


#Grafico



if st.checkbox("Ver gráfico de Tendencia"):
    Año_minimo = st.slider("Definir año mínimo", 1920, 2021, 1920)
    Año_maximo = st.slider("Definir año máximo", 1920, 2021, 2021)

    # Ordenar el dataframe por el año
    df_accidentes = df_accidentes.sort_values('Año')

    # Crear la gráfica de línea suavizada
    fig, ax = plt.subplots()
    sns.lineplot(data=df_accidentes[(df_accidentes["Año"] >= Año_minimo) & (df_accidentes["Año"] <= Año_maximo)], x='Año', y='Tasa_Mortalidad', ax=ax)

    # Establecer etiquetas y título de la gráfica
    ax.set_xlabel('Año')
    ax.set_ylabel('Tasa de Mortalidad')
    ax.set_title('Tendencia de la Tasa de Mortalidad por Año')

    # Mostrar la gráfica en Streamlit
    st.pyplot(fig)

    
    



        


