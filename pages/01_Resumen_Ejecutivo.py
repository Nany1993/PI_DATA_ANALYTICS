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

st.markdown("*En cada pagina adicional a este informe se detallan los indicadores*")

st.markdown("**Hallazgos importantes:**")
st.markdown('''**Explorando la información se visualizaron algunos valores atipicos que están por encima del umbral máximo , 
            lo que indica que:**
* *El 10% (508) de los accidentes tuvieron más de 600 personas a bordo entre pasajeros y tripulantes*
* *El 10%(500) de los accidentes tuvieron más de 600 pasajeros*
* *El 3%(151) de los acciendentes contaban con una tripulación de más de 80 personas*
* *El 9%(454) de los accidentes presentó más de 580 fallecidos*
* *El 9%(450) de los accidentes presentó más de 560 pasajeros fallecidos*
* *El 2.4%(122) de los accidentes presentó más de 40 tripulantes fallecidos*
* *El 5%(248) de los accidentes fueron una gran catastrofe con más de 2750 muertos en tierra.*
*El 11 de septiembre de 2001 se puede relacionar con los ataques terroristas en Estados Unidos, 
donde varios aviones comerciales fueron secuestrados y utilizados como armas.*
* *Las horas en que más suceden los accidentes son despúes del medio dia (11:00), 
* *las top 5 son: 15:00, 14:00, 11:00, 17:00 y 16:00.*
* *las aerolineas con más accidentes presentados, top 5 con más de 45 accidentes: Aeroflot, Military U.S Air Force, 
Air France, Deutsche Lufthansa y United Air Lines.*
* *Las 3 rutas de vuelo con más accidentes corresponden a: Training, sightseeing y Testflight*
* *Al analizar los datos, se destaca que los aviones Douglas DC-3, de Havilland Canada DHC-6 Twin Otter 300, 
Douglas C-47A, Douglas C-47 y Douglas DC-4 son prominentes en la lista de aviones con más accidentes.*
''')

st.markdown("**Conclusiones y recomendaciones**")

st.markdown('''*1- El 2001 fue el unico año con gran impacto a nivel de mortalidad, lo cual se relaciona con el 
            secuestro de los aviones por parte de grupos terroristas en estados unidos, la catastrofe de las 
            torres gemelas*''')
st.markdown('''*2- Una conclusión interesante es que las rutas de vuelo con más accidentes son aquellas relacionadas 
            con actividades específicas de la aviación, como entrenamiento, turismo de observación y 
            vuelos de prueba.*
            *Esto sugiere que estas actividades pueden presentar desafíos adicionales o 
            mayores riesgos en comparación con otras operaciones aéreas 
            El hecho de que la ruta de vuelo de entrenamiento tenga una alta incidencia de accidentes puede indicar 
            que el proceso de formación de pilotos y tripulación de vuelo puede ser crítico en términos de 
            seguridad y requiere una atención especial para minimizar los riesgos.*''')

st.markdown('''*3 -Existe una fuerte correlación entre las personas que abordan un avión y las personas que fallecen
            en un accidente, es decir entre más personas a bordo más muertes dado un accidente, por eso es importante
            considerar el número de personas a bordo, tanto pasajeros como tripulantes, 
            en relación con los resultados de seguridad en los accidentes aéreos. Estos factores pueden desempeñar 
            un papel significativo en la gravedad de las consecuencias de un accidente y deben ser tenidos en 
            cuenta en la planificación y gestión de la seguridad aérea.* ''')
            
