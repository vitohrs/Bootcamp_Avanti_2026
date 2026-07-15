# ATIVIDADE 2
# 9 QUESTÃO: Utilizando pandas, como selecionar uma coluna específica e filtrar linhas em um “DataFrame” com base em uma condição?

import pandas as pd

df = pd.read_csv("deuses.csv")

deusesEsquerda = df[df["direção"] == 'esquerda']
print("Deuses de esquerda")
print(deusesEsquerda)

deusesmenos20 = df[df["idade"] < 20]
print("\nDeuses menores de 20 anos")
print(deusesmenos20)

