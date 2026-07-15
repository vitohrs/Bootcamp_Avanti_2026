# ATIVIDADE 2
# 6 QUESTÃO: Como identificar e tratar outliers em uma coluna numérica usando desvio padrão ou quartis?

import pandas as pd

df = pd.DataFrame({
    "numeros1": [25, 24, 28, 29, 30, 21, 24, 25, 55],
    "numeros2": [30, 42, 51, 33, 54, 45, 80, 66, 500]
})

# IDENTIFICANDO OUTLIER UTILIZADO DESVIO PADRÃO
media = df["numeros1"].mean()
desvio = df["numeros1"].std()

outliers = df[
    (df["numeros1"] > media + 2 * desvio) |
    (df["numeros1"] < media - 2 * desvio)
]

print("Outlier (Desvio padrão):", outliers["numeros1"].values)

# IDENTIFICANDO OUTLIER UTILIZADO QUARTIS

Q1 = df["numeros2"].quantile(0.25)
Q3 = df["numeros2"].quantile(0.75)

IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers = df[
    (df["numeros2"] < limite_inferior) |
    (df["numeros2"] > limite_superior)
]

print("Outlier (IQR):", outliers["numeros2"].values)