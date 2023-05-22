import streamlit as st
import pandas as pd 


df_accidentes = pd.read_csv("df_accidente3.csv", sep=",")

st.title("INFORME ACCIDENTES AÉREOS")
st.markdown('***')

st.write('''Los accidentes aéreos son eventos no deseados que causan daños a personas y aeronaves. 
         Pueden ser causados por errores humanos, fallas de equipos, condiciones meteorológicas, 
         problemas de mantenimiento y más. El análisis de datos históricos de accidentes aéreos es vital 
         para mejorar la seguridad en la aviación, identificando patrones y tendencias. Esto ayuda a mejorar la 
         capacitación, el diseño de aeronaves y la gestión del tráfico aéreo. La recopilación y 
         análisis sistemático de estos datos contribuyen a prevenir futuros accidentes y mejorar la seguridad 
         en la industria aérea.''')

st.markdown("**En este informe se estudia el comportamiento de los accidentes aéreos a través de la historia**")
st.markdown("**Para ello se plantean los siguientes KPI:**")
st.markdown("- Tasa de Mortalidad Anual")
st.markdown("- Indice de Mejora de la seguridad Anual")
st.markdown("- Indice de Supervivencia Anual")
st.markdown("- Tasa de accidentalidad en actividades especificas de la aviación")