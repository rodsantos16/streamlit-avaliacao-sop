import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("Análise Financeira - MS Sample")

# Carregar o CSV
df = pd.read_csv("MS_Financial Sample.csv")


st.subheader("Visualização da Tabela")
st.dataframe(df)

# Gráfico de Receita (Sales) por Segmento
st.subheader("Receita Total por Segmento")

sales_by_segment = df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)

fig, ax = plt.subplots()
sales_by_segment.plot(kind="bar", ax=ax)
ax.set_ylabel("Total de Vendas")
ax.set_xlabel("Segmento")
plt.xticks(rotation=45)
st.pyplot(fig)
