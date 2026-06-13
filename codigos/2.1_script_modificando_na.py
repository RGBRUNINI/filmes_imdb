
"""
Contexto: O que temos no dataset
Olhando o filmes_imdb.xlsx, temos alguns casos perfeitos para praticar:

---------------------------------------------------------------------
Linha  | (index)	| Filme	                 | Problema
---------------------------------------------------------------------
36     | (row 37)	| Inglourious Basterds   | bilheteria_dolares vazia
42     | (row 43)	| Pulp Fiction	         | duracao_min vazia
46     | (row 47)	| Forrest Gump	         | data_lancamento vazia
49     | (row 50)	| (título vazio)         | titulo vazio
---------------------------------------------------------------------

Obs.: Note que são problemas pontuais, ou seja, apenas um valor errado ou ausente em cada linha. 
Isso é ótimo para praticar a modificação de células específicas usando .loc[].

"""

# MÉTODOS/FORMAS POSSÍVEIS DE RESOLVE RO PROBLEMA 


"""
============================================================
SCRIPT: Tratamento de dados pontuais no dataset filmes_imdb
============================================================

OBJETIVO:
Corrigir valores ausentes (NaN) ou inconsistentes em linhas específicas
do dataset utilizando diferentes abordagens do Pandas.

ESTRATÉGIAS ABORDADAS:
1. Edição direta por índice com .loc[]
2. Localização dinâmica por conteúdo (filtro)
3. Atualização segura apenas quando o valor está vazio (NaN)

IMPORTANTE:
- O DataFrame é carregado UMA única vez (evita perda de estado)
- Sempre validamos filtros antes de acessar .index[0]
"""

# ============================================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ============================================================

import pandas as pd
import numpy as np


# ============================================================
# CARREGAMENTO DO DATAFRAME
# ============================================================

"""
Carrega o arquivo Excel para um DataFrame Pandas.

ATENÇÃO:
Este carregamento deve ser feito apenas uma vez.
Recarregar o DataFrame no meio do script faz perder alterações anteriores.
"""

caminho = r"dados\dados_excel\filmes_imdb.xlsx"
df_imdb = pd.read_excel(caminho)


# ============================================================
# MÉTODO 1 — MODIFICAÇÃO DIRETA USANDO ÍNDICE (.loc)
# ============================================================

"""
Neste método, usamos o índice da linha diretamente.

SINTAXE:
df.loc[indice_linha, 'nome_coluna'] = novo_valor

VANTAGENS:
- Simples e direto
- Mais rápido quando o índice é conhecido

DESVANTAGEM:
- Depende de conhecer o índice exato da linha
"""

print("\n========== MÉTODO 1 ==========")

# CASO 1: Corrigir bilheteria ausente
df_imdb.loc[36, 'bilheteria_dolares'] = 321500000

# CASO 2: Corrigir duração ausente
df_imdb.loc[42, 'duracao_min'] = 154

# CASO 3: Corrigir data de lançamento ausente
df_imdb.loc[46, 'data_lancamento'] = pd.Timestamp('1994-07-06')

# CASO 4: Corrigir título vazio
df_imdb.loc[49, 'titulo'] = 'Desconhecido'

# Visualização das alterações
print(df_imdb.loc[[36, 42, 46, 49],
      ['titulo', 'bilheteria_dolares', 'duracao_min', 'data_lancamento']])


# ============================================================
# MÉTODO 2 — LOCALIZAÇÃO POR CONTEÚDO (FILTRO)
# ============================================================

"""
Neste método, não usamos o índice diretamente.
Primeiro encontramos a linha com base em um valor (ex: título),
depois utilizamos o índice encontrado para editar.

PASSOS:
1. Criar um filtro (condição)
2. Validar se encontrou alguma linha
3. Pegar o índice com .index[0]
4. Aplicar a modificação com .loc[]

VANTAGENS:
- Mais flexível
- Funciona mesmo sem saber o índice

CUIDADO:
- Sempre verificar se o filtro NÃO está vazio
"""

print("\n========== MÉTODO 2 ==========")

# ------------------------------------------------------------
# EXEMPLO 1: Inglourious Basterds
# ------------------------------------------------------------

filtro = df_imdb[df_imdb['titulo'] == 'Inglourious Basterds']

if not filtro.empty:
    indice = filtro.index[0]

    df_imdb.loc[indice, 'bilheteria_dolares'] = 321500000

    print(f"Filme corrigido no índice: {indice}")
    print(df_imdb.loc[indice, ['titulo', 'bilheteria_dolares']])
else:
    print("Filme 'Inglourious Basterds' não encontrado")


# ------------------------------------------------------------
# EXEMPLO 2: Linha com título 'Desconhecido'
# ------------------------------------------------------------

filtro_unknown = df_imdb[df_imdb['titulo'] == 'Desconhecido']

if not filtro_unknown.empty:
    indice_unknown = filtro_unknown.index[0]

    df_imdb.loc[indice_unknown,
                ['nome_pais', 'continente', 'idioma_principal']] = [
        'França',
        'Europa',
        'Francês'
    ]

    print("\nLinha 'Desconhecido' após correção:")
    print(df_imdb.loc[indice_unknown,
          ['titulo', 'nome_pais', 'continente', 'idioma_principal']])
else:
    print("Nenhuma linha com título 'Desconhecido' encontrada")


# ============================================================
# MÉTODO 3 — PREENCHIMENTO SEGURO (SOMENTE SE NaN)
# ============================================================

"""
Neste método, garantimos que só alteramos a célula se ela estiver vazia.

FUNÇÃO UTILIZADA:
pd.isna(valor)

RETORNA:
- True  → valor é NaN, None ou NaT
- False → valor já existe

VANTAGEM:
- Evita sobrescrever dados válidos
"""

print("\n========== MÉTODO 3 ==========")

linha = 36
coluna = 'bilheteria_dolares'

if pd.isna(df_imdb.loc[linha, coluna]):
    df_imdb.loc[linha, coluna] = 321500000
    print(f"Célula preenchida na linha {linha}")
else:
    print(f"Linha {linha} já possui valor: {df_imdb.loc[linha, coluna]}")

# Visualização da linha completa
print("\nLinha completa após verificação:")
print(df_imdb.loc[linha])


# ============================================================
# SALVANDO O RESULTADO (OPCIONAL)
# ============================================================

"""
Salva o DataFrame tratado em um novo arquivo Excel.

IMPORTANTE:
- index=False evita salvar a coluna de índice no arquivo
"""

# df_imdb.to_excel(
#     r"dados\dados_excel\filmes_imdb_tratado.xlsx",
#     index=False
# )


# ============================================================
# RESUMO FINAL
# ============================================================

"""
QUANDO USAR CADA MÉTODO:

✔ Método 1 (.loc com índice)
→ Quando você sabe exatamente a linha

✔ Método 2 (filtro + index)
→ Quando você conhece um valor (ex: título), mas não o índice

✔ Método 3 (pd.isna)
→ Quando quer evitar sobrescrever dados existentes

REGRA DE OURO:
Nunca use .index[0] sem garantir que o filtro NÃO está vazio.
"""

print("\n========== FIM DO SCRIPT ==========")


"""

Resumo Visual — Quando usar cada método
---------------------------------------------------------------------:
# ✅ Você SABE o índice e quer editar 1 coluna
df_imdb.loc[36, 'bilheteria_dolares'] = 321500000

# ✅ Você SABE o índice e quer editar VÁRIAS colunas de uma vez
df_imdb.loc[36, ['nome_pais', 'continente']] = ['França', 'Europa']

# ✅ Você NÃO sabe o índice — localiza pelo título primeiro
idx = df_imdb[df_imdb['titulo'] == 'Inglourious Basterds'].index[0]
df_imdb.loc[idx, 'bilheteria_dolares'] = 321500000

# ✅ Quer editar SOMENTE SE estiver vazio (mais seguro)
if pd.isna(df_imdb.loc[36, 'bilheteria_dolares']):
    df_imdb.loc[36, 'bilheteria_dolares'] = 321500000

"""