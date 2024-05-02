import streamlit as st

# Importando os dados
import pandas as pd
import matplotlib.pyplot as plt

st.title("Testando algumas funcionalidades")

st.markdown("# Chamando uma DataFrame:")
link = "https://raw.githubusercontent.com/gfsilveira/ebac/main/"
link += "03-Cientista%20de%20Dados/02-Crisp-DM/010_m%C3%B3dulo/"
link += "Profissao-%20Cientista%20de%20Dados_M10_support%20material.csv"

df = pd.read_csv(link)
df.drop(["Unnamed: 0","index","data_ref"], axis=1, inplace=True)
df = df.dropna()
st.write(df)
st.markdown("---")

st.markdown("# Gráfico com Streamlit")
st.line_chart(df.qtd_filhos)
st.markdown("---")

st.markdown("# Gráfico com Pandas")
fig = plt.figure(figsize=(10,5))
plt.title("Gráfico quantidade de filhos")
df.qtd_filhos.plot(kind="hist")
plt.xlabel("Quantidade de filhos")
plt.ylabel("Frequência")
st.pyplot(fig)
st.markdown("---")