import streamlit as st
import pandas as pd

from price_analyzer import analisar_preco, limpar_precos


st.set_page_config(
    page_title="Analisador de Preços",
    page_icon="💰",
    layout="centered"
)

st.title("Analisador de Preços com Mediana das Medianas")

st.write(
    "Digite **valores de referência** de um mesmo produto e informe o **preço que deseja analisar**. "
    "O sistema irá calcular a mediana desses valores para, dessa forma, indicar se o preço está **abaixo**, **acima** "
    "ou **próximo** do valor esperado de mercado."
)

st.subheader("Preços de referência")

texto_precos = st.text_area(
    "Digite os preços separados por vírgula ou linha:",
    placeholder="4200, 5700, 4600, 8000, 3900",
    height=150
)

preco_analisado = st.number_input(
    "Preço que deseja analisar:",
    min_value=0.0,
    step=10.0,
    format="%.2f"
)

if st.button("Analisar preço"):
    try:
        precos = limpar_precos(texto_precos)

        if len(precos) < 2:
            st.error("Digite pelo menos dois valores de referência.")
        else:
            resultado = analisar_preco(precos, preco_analisado)

            st.subheader("Resultado da análise")

            col1, col2, col3 = st.columns(3)

            col1.metric("Mediana", f"R$ {resultado['mediana']:.2f}")
            col2.metric("Diferença", f"R$ {resultado['diferenca']:.2f}")
            col3.metric("Variação", f"{resultado['percentual']:.2f}%")

            st.success(f"Classificação: {resultado['classificacao']}")

            df = pd.DataFrame({
                "Preços de referência": precos
            })

            st.subheader("Dados informados")
            st.dataframe(df)

            st.subheader("Conclusão")

            st.write(f"""
            - O preço analisado foi **R$ {preco_analisado:.2f}**

            - A mediana dos preços de referência é **R$ {resultado['mediana']:.2f}**

            - Portanto, o sistema classificou esse preço como: **{resultado['classificacao']}**
            """)

    except ValueError as erro:
        st.error(str(erro))
