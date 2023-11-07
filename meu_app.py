import streamlit as st
import pandas as pd

st.set_page_config(page_title="Meu site Streamlit")

with st.container():
    st.subheader("Meu primeiro site com o Streamlit")
    st.title("Dashboard de contratos")
    st.write("Informações sobre os contratos fechados pela Hash&Co ao longo da vida.")
    st.write("Quer aprender Python? [Clique Aqui](https://www.hashtagtreinamentos.com/curso-python)")


@st.cache_data
def carregar_dados():
    tabela = pd.read_csv("resultados.csv")
    return tabela


with st.container():
    st.write("---")
    dados = carregar_dados()
    st.area_chart(dados, x="Data", y="Contratos")
