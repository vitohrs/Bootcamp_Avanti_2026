# ATIVIDADE 2
# 7 QUESTÃO: Como concatenar vários DataFrames (empilhando linhas ou colunas),mesmo que tenham colunas diferentes?

import pandas as pd

df1 = pd.DataFrame({
    "Nome": ["Zagreus", "Hermes"],
    "Seguidores": [3333, 3440],
    "idade": [50, 60]
})

df2 = pd.DataFrame({
    "Nome": ["Zeus", "Artemis"],
    "Seguidores": [2222, 1118]
})

resposta = pd.concat([df1, df2],ignore_index=True)

print(resposta)