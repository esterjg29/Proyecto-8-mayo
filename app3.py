import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

wage = pd.read_csv("Salarios.csv")

st.title("Salarios")

tab1, tab2 = st.tabs(["Tab1", "Tab2"])

with tab1:
    fig, ax = plt.subplots(1, 4, figsize=(10, 4))
    ax[0].hist(wage["Salario"])
    conteo = wage["Educación"].value_counts()
    ax[1].bar(conteo.index, conteo.values)
    ax[2].hist(wage["Sexo"])
    conteo = wage["Estado civil"].value_counts()
    ax[3].bar(conteo.index, conteo.values)
    fig.tight_layout()
    st.pyplot(fig)

with tab2:
    fig, ax = plt.subplots(1, 3, figsize=(10, 4))
    sns.scatterplot(data=wage, x="Salario", y="Educación", ax=ax[0])
    sns.boxplot(data=wage, x="Sexo", y="Salario", ax=ax[1])
    sns.scatterplot(data=wage, x="Salario", y="Estado civil", ax=ax[2])
    fig.tight_layout()
    st.pyplot(fig)