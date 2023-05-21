import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_accidentes = pd.read_csv("df_accidente2.csv", sep=",")

st.title("DASHBOARD ACCIDENTES AÉREOS")

