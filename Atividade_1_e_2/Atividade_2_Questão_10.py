# ATIVIDADE 2
# 10 Questão: Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?

import pandas as pd

df = pd.read_csv("deuses.csv")

#Indica quais valores são NaN
print(df.isna())

#Uma opção é remover instancias que contenham valores NaN

#Remove linhas que possuem algum valor igual a NaN
df_sem_nan = df.dropna()

print(df_sem_nan)

#Outra opção é utilizar um valor fixo para substituir valores NaN

df["direção"] = df["direção"].fillna("Não consta")

#Outra opção é utilizar a média da coluna para preencher o valor faltante

media = df["idade"].mean()

df["idade"] = df["idade"].fillna(media)

print(df)
