# ATIVIDADE 2
# 8 QUESTÃO: Utilizando pandas, como realizar a leitura de um arquivo CSV em um DataFrame e exibir as primeiras linhas?

import pandas as pd

df = pd.read_csv("deuses.csv")

# Exibir as 5 primeiras linhas do DataFrame
print(df.head())