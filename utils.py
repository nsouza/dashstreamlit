from dataset import df
import pandas as pd
import streamlit as st
import time

def format_number(value,  prefix = ''):
    for unit in ['', 'mil']:
        if value < 1000:
            return f"{prefix} {value:.2f} {unit}"
        value /= 1000
    return f"{prefix} {value:.2f} milhões"



# 1- Dataframe Receitas por estado
df_rec_estado = df.groupby('Local da compra')[['Preço']].sum()
df_rec_estado = df.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']] \
    .merge(df_rec_estado, left_on='Local da compra', right_index=True) \
    .sort_values('Preço', ascending=False)
    
# 2 - Dataframa Receitas Mensal
df_rec_mensal = df.set_index('Data da Compra').groupby(pd.Grouper(freq='M'))['Preço'].sum().reset_index()
df_rec_mensal['Ano'] = df_rec_mensal['Data da Compra'].dt.year
df_rec_mensal['Mês'] = df_rec_mensal['Data da Compra'].dt.month_name()

#print(df_rec_mensal)

# 3 - Dataframe receita por categoria
df_rec_categoria = (
    df.groupby('Categoria do Produto')[['Preço']]
    .sum()
    .sort_values('Preço', ascending=False)
)

# 4 - Dataframe vendedores
df_vendedores = (
    pd.DataFrame(df.groupby('Vendedor')['Preço']
    .agg(['sum', 'count']))
)

#Função para converter arquivo csv
@st.cache_data
def convert_csv(df):
    return df.to_csv(index=False).encode('utf-8')

def mensagem_sucesso():
    sucess = st.success(
        'Arquivo baixado com sucesso! :white_check_mark:',
        icon=':tada:'
    )
    time.sleep(3)
    sucess.empty()
  


