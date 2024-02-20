import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles.csv')  # lendo os dados
hist_button = st.button('Criar histograma')  # criar um botão
graf_box = st.checkbox('Gráfico dispesão')

st.header('Dados Veículos')
if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

    if graf_box:  # se o botão for clicado
    # escrever uma mensagem
        st.write(
        'Criando gráfico dispersão conjunto venda de carros')

    # criar um gráfico de dispersão
        fig1 = px.scatter(car_data, x="odometer", y="price")

    # exibir um gráfico Plotly interativo
        st.plotly_chart(fig1, use_container_width=True)