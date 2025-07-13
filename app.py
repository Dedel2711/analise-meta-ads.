# analise-meta-ads.
import streamlit as st
import pandas as pd

# Função para gerar insights
def gerar_insights(df):
    insights = []

    for _, row in df.iterrows():
        nome = row['campaign_name']
        ctr = row['ctr']
        cpc = row['cpc']
        roas = row['roas']
        spend = row['spend']
        purchases = row['purchases']

        if roas < 1:
            insights.append(f"🚫 A campanha '{nome}' teve ROAS {roas:.2f}. Está dando prejuízo. Considere pausar ou otimizar.")
        elif roas >= 2:
            insights.append(f"✅ A campanha '{nome}' teve ROAS {roas:.2f}. Excelente performance, ideal para escalar.")
        elif 1 <= roas < 2:
            insights.append(f"⚠️ A campanha '{nome}' está no limite com ROAS {roas:.2f}. Monitorar de perto.")

        if ctr < 1:
            insights.append(f"📉 CTR de '{nome}' está abaixo de 1%. Pode indicar criativo fraco ou público errado.")
        elif ctr > 2:
            insights.append(f"🔥 A campanha '{nome}' tem ótimo CTR de {ctr:.2f}%. Público bem engajado!")

        if cpc > 10:
            insights.append(f"💸 Custo por clique da campanha '{nome}' está alto (R${cpc:.2f}).")

        if spend > 1000 and purchases == 0:
            insights.append(f"🚨 '{nome}' gastou R${spend:.2f} e não gerou compras. Verifique urgência.")

    return insights

st.title("IA Análise de Campanhas Meta Ads")

uploaded_file = st.file_uploader("Faça upload do CSV das campanhas", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Dados carregados:")
    st.dataframe(df)

    insights = gerar_insights(df)
    st.write("### 🔎 Insights gerados:")
    for insight in insights:
        st.write(insight)
![andrew-kliatskyi-d3YXpAqdy2I-unsplash](https://github.com/user-attachments/assets/1f570828-138a-4d81-8a73-f690b48a970f)
