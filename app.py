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
import streamlit as st
import pandas as pd

def gerar_insights_engajamento(df):
    insights = []

    for _, row in df.iterrows():
        nome = row['campaign_name']
        ctr = row.get('ctr', None)
        cpc = row.get('cpc', None)
        spend = row.get('spend', None)
        new_followers = row.get('new_followers', None)  # Supondo que tenha essa coluna
        reactions = row.get('reactions', None)          # Curtidas, likes, etc
        comments = row.get('comments', None)
        shares = row.get('shares', None)

        # Avaliar CTR
        if ctr is not None:
            if ctr < 1:
                insights.append(f"📉 Campanha '{nome}': CTR baixa ({ctr:.2f}%), indicando pouco engajamento.")
            elif ctr > 2:
                insights.append(f"🔥 Campanha '{nome}': Ótimo engajamento com CTR de {ctr:.2f}%.")

        # Avaliar CPC
        if cpc is not None and cpc > 10:
            insights.append(f"💸 Campanha '{nome}': CPC alto (R${cpc:.2f}), pode indicar custo alto para engajamento.")

        # Seguidores novos
        if new_followers is not None:
            if new_followers > 20:
                insights.append(f"✅ Campanha '{nome}': Gerou {int(new_followers)} seguidores novos, ótimo resultado!")
            elif new_followers == 0:
                insights.append(f"⚠️ Campanha '{nome}': Não gerou seguidores novos.")

        # Reações, comentários, compartilhamentos (se dados disponíveis)
        if reactions is not None and reactions < 10:
            insights.append(f"📉 Campanha '{nome}': Poucas reações ({int(reactions)}).")
        if comments is not None and comments < 5:
            insights.append(f"📉 Campanha '{nome}': Poucos comentários ({int(comments)}).")
        if shares is not None and shares < 3:
            insights.append(f"📉 Campanha '{nome}': Poucos compartilhamentos ({int(shares)}).")

        # Aviso sobre gasto sem resultado
        if spend is not None and spend > 1000 and (new_followers == 0 or (reactions is not None and reactions < 10)):
            insights.append(f"🚨 Campanha '{nome}': Gasto alto (R${spend:.2f}) com pouco retorno em engajamento e seguidores.")

    return insights

st.title("IA Análise de Campanhas Meta Ads - Seguidores & Engajamento")

uploaded_file = st.file_uploader("Faça upload do CSV das campanhas", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file, encoding='latin1')
    st.write("### Dados carregados:")
    st.dataframe(df)

    insights = gerar_insights_engajamento(df)
    st.write("### 🔎 Insights gerados:")
    for insight in insights:
        st.write(insight)
