import streamlit as st

st.title("Streamlit")
st.header("Header")
st.subheader("subheader".title())

st.markdown("# Markdown :sunglasses:")
st.write("## Write")
st.markdown("---")
st.markdown("# Markdown")
st.markdown("## Markdown")
st.markdown("Markdown")
st.markdown("*Markdown*")
st.markdown("**Markdown**")
st.markdown("`Markdown`")
st.markdown("__*Markdown*__")
st.markdown("Endereço [Streamlit](https://streamlit.io/)")

st.markdown("---")
texto = '''
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
'''
texto = f"<h1 style='text-align: justify; color: red' >{texto}</h1>"
st.markdown(f"{texto}", unsafe_allow_html=True)
st.markdown("---")
st.write("Write")
st.write("Write")
st.markdown("Olá Streamlit :sunglasses:")
st.markdown("---")
st.markdown("## Tabela")
tabela = '''
Entrada 1 | Entrada 2 | Entrada 3 |
---   |---    |---
Cel 1 | Cel 2 | Cel 3
'''
st.markdown(f"{tabela}")
st.markdown("---")