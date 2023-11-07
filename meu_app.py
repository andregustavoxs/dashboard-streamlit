import streamlit as st

st.set_page_config(page_title = "Meu site Streamlit")

with st.container():
    st.subheader("Meu primeiro site com o Streamlit")
    st.title("Dashboard de contratos")
    st.write("Informações sobre os contratos fechados pela Hash&Co ao longo da vida.")
    st.write("Quer aprender Python? [Clique Aqui](https://www.hashtagtreinamentos.com/curso-python)")

with st.container():
    st.write("---")

print("Hello World!")