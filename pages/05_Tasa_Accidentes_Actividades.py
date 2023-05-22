import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

st.title("Tasa de accidentes en actividades de la aviación")
st.markdown("**Descripción**")
st.write("Porcentaje de accidentes en las rutas Training, sightseeing y Testflight")
st.markdown("**Fórmula de medición**")
st.write("(Total_accidentes_rutas_actual - Total_accidentes_rutas_año_anterior  / Total_accidentes_rutas_año_anterior ) * 100")
st.markdown("**KPI**")
st.write("Disminuir la tasa de accidentalidad en actividades de la aviación en un 10% anualmente")

# Cargar dataframe con las columnas necesarias
columnas = ["Año", "Tasa_Mortalidad", "Total_Fallecidos", "Total_A_bordo", "Muertos_en_tierra", "resumen", "Ruta Detallada"]
df_accidentes = pd.read_csv("df_accidente3.csv", sep=",", usecols=columnas)
df_accidentes.dropna(inplace=True)
df_accidentes = df_accidentes[df_accidentes["Ruta Detallada"].isin(["Training", "Sightseeing", "Test flight"])]


#Creamos columna Sobrevivientes
df_accidentes["Sobrevivientes"] = df_accidentes["Total_A_bordo"] - df_accidentes["Total_Fallecidos"]

# Convertir la columna "Año" a tipo entero
df_accidentes['Año'] = df_accidentes['Año'].astype(int)

# Reordenar las columnas
columnas_reordenadas = ["Año","Ruta Detallada", "Sobrevivientes", "Total_Fallecidos", "Muertos_en_tierra", "resumen"]
df_accidentes = df_accidentes[columnas_reordenadas]

if st.checkbox("Ver información detallada por las rutas con mayor accidentalidad"):
    st.dataframe(df_accidentes)

#Tasa de accidentalidad ruta
   
if st.checkbox("Tabla resumen de la Tasa de accidentalidad año a año"):
    

    # Agrupar los datos por año y ruta detallada y contar la frecuencia
    tabla_tasa_accidentalidad = df_accidentes.groupby(['Año', 'Ruta Detallada']).size().unstack()

    # Renombrar las columnas de la tabla
    tabla_tasa_accidentalidad.columns = ['Ruta Training', 'Ruta Sightseeing', 'Ruta Test flight']

    # Mostrar la tabla resultante
    st.table(tabla_tasa_accidentalidad)

   

#Grafico
if st.checkbox("Ver Gráfico de dispersion"):
    # Obtener la lista de rutas únicas
    rutas_unicas = df_accidentes['Ruta Detallada'].unique().tolist()

    # Checkbox para seleccionar las rutas a mostrar
    rutas_seleccionadas = st.multiselect("Seleccionar Rutas", rutas_unicas)

    # Sliders para seleccionar el rango de años
    Año_minimo = st.slider("Definir año mínimo", 1920, 2021, 1920)
    Año_maximo = st.slider("Definir año máximo", 1920, 2021, 2021)

    # Filtrar los datos dentro del rango de años seleccionado y las rutas seleccionadas
    df_filtrado = df_accidentes[(df_accidentes['Año'] >= Año_minimo) & (df_accidentes['Año'] <= Año_maximo) & (df_accidentes['Ruta Detallada'].isin(rutas_seleccionadas))]

    # Obtener la frecuencia de las rutas por año
    frecuencia_rutas_por_año = df_filtrado.groupby(['Año', 'Ruta Detallada']).size().reset_index(name='Frecuencia')

    # Crear una paleta de colores para las rutas seleccionadas
    colores = sns.color_palette("viridis", n_colors=len(rutas_seleccionadas))

    # Crear el gráfico de dispersión
    fig, ax = plt.subplots()
    for i, ruta in enumerate(rutas_seleccionadas):
        datos_ruta = frecuencia_rutas_por_año[frecuencia_rutas_por_año['Ruta Detallada'] == ruta]
        ax.scatter(datos_ruta['Año'], datos_ruta['Frecuencia'], color=colores[i], label=ruta)

    # Configurar los ejes y el título
    ax.set_xlabel('Año')
    ax.set_ylabel('Cantidad de accidentes')
    ax.set_title('Accidentalidad por Rutas por Año')

    # Agregar leyenda
    ax.legend()

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)




