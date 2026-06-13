#Exploração Inicial dos Dados
#Objetivo: Entender a estrutura do dataset antes de qualquer limpeza. Nunca limpe o que você não conhece.


# ============================================================
# EXERCÍCIO 1 — Exploração Inicial
# ============================================================

# Importando as bibliotecas necessárias
import pandas as pd  # Pandas: biblioteca principal para manipulação de dados em tabelas
import numpy as np

# Definindo o caminho do arquivo Excel
caminho = r"dados\dados_excel\filmes_imdb.xlsx"

# Lendo o arquivo Excel e armazenando em um DataFrame
# Um DataFrame é como uma tabela do Excel dentro do Python
df_imdb = pd.read_excel(caminho)


# -----------------------------------------------------------
# 1.1 Visualizando as primeiras linhas
# head(10) mostra as 10 primeiras linhas da tabela
# Útil para ter uma visão geral do conteúdo
# -----------------------------------------------------------
print("=== PRIMEIRAS 10 LINHAS ===")

print(df_imdb.head(300))


# -----------------------------------------------------------
# 1.2 Verificando informações estruturais da tabela
# info() mostra: nome das colunas, tipo de dado e quantidade
# de valores não-nulos (non-null) em cada coluna
# Se non-null < total de linhas → há valores ausentes!
# -----------------------------------------------------------
print("\n=== INFORMAÇÕES DO DATAFRAME ===")
print(df_imdb.info())

# -----------------------------------------------------------
# 1.3 Verificando o tamanho da tabela
# shape retorna uma tupla: (número de linhas, número de colunas)
# -----------------------------------------------------------
print("\n=== TAMANHO DA TABELA (linhas, colunas) ===")
print(df_imdb.shape)

# -----------------------------------------------------------
# 1.4 Verificando estatísticas básicas das colunas numéricas
# describe() calcula: contagem, média, desvio padrão,
# mínimo, máximo e quartis automaticamente
# Muito útil para identificar valores absurdos (outliers)
# -----------------------------------------------------------
print("\n=== ESTATÍSTICAS DAS COLUNAS NUMÉRICAS ===")
print(df_imdb.describe())

# -----------------------------------------------------------
# 1.5 Contando valores nulos por coluna
# isnull() marca cada célula como True (nulo) ou False (preenchido)
# sum() soma os True de cada coluna → total de nulos por coluna
# -----------------------------------------------------------
print("\n=== VALORES NULOS POR COLUNA ===")
print(df_imdb.isnull().sum())

#=================

#O que observar no resultado:

# Colunas com Non-Null Count < 100 têm dados faltando
# No describe(), veja o max de rating_imdb — vai aparecer um valor absurdo como 20
# No describe(), veja o min de duracao_min — pode aparecer 0 ou erro

#=================

# Verificar se há nomes errados nas colunas

print(df_imdb['genero'].unique().tolist())


# Padronizar os nomes errados

df_imdb['genero'] = df_imdb['genero'].replace(
    {'Crime': 'Crime', 
 'Action': 'Ação', 
 'Drama': 'Drama', 
 'Sci-Fi': 'Ficção', 
 'SciFi': 'Ficção', 
 'Fantasy': 'Fantasia', 
 'Fantasia': 'Fantasia', 
 'Science Fiction': 'Ficção', 
 'Thriller': 'Terror', 
 'Thriler': 'Terror', 
 'Adventure': 'Aventura', 
 'Animation': 'Animação', 
 'Romance': 'Romance', 
 'Anim': 'Animação', 
 'Comedy': 'Comédia', 
 'War': 'Guerra', 
 'Western': 'Velho Oeste', 
 'Musical': 'Musical', 
 'ACTION': 'Ação', 
 'Science-Fiction': 'Ficção', 
 'Unknown': 'Desconhecido', 
 'Acton': 'Ação', 
 'Ação': 'Ação', 
 'Comédia': 'Comédia', 
 'Biografia': 'Biografia', 
 'Ficção': 'Ficção', 
 'Animação': 'Animação', 
 'Aventura': 'Aventura', 
 'Guerra': 'Guerra', 
 'Documentário': 'Documentário', 
 'Suspense': 'Suspense', 
 'Família': 'Família', 
 'Mistério': 'Mistério', 
 'Terror': 'Terror'})

print(df_imdb['moeda'].unique().tolist())


df_imdb['moeda'] = df_imdb['moeda'].replace(
  {'Dólar Americano' : 'Dólar', 
   'Dólar Neozelandês': 'Dólar', 
   'Euro': 'Euro', 
   'Dólar Australiano': 'Dólar', 
   np.nan : 'Desconhecido', 
   'Zloty': 'Zloty', 
   'Real' : 'Real', 
   'Iene' : 'Iene', 
   'Won' : 'Won', 
   'Libra Esterlina' : 'Libra', 
   'Dólar' : 'Dólar', 
   'Libra' : 'Libra', 
   'Dólar neozelandês': 'Dólar'})

print(df_imdb['moeda'].unique().tolist())

