# ATIVIDADE 2
# 5 QUESTÃO: Crie uma função que receba uma lista de tuplas, cada uma contendo o nome e a idade de uma pessoa,
# e retorne a lista ordenada pelo nome das pessoas em ordem alfabética. 

pessoas = [
    ("Anastasia", 25),
    ("Hermes", 31),
    ("Zagreus", 19),
    ("Heres", 42),
    ("Zeus", 28),
    ("Artemis", 35)
]
def OrdernaLista (list):
    listaOrdenada = list.copy()
    listaOrdenada.sort()
    return listaOrdenada

resposta = OrdernaLista(pessoas)

print(resposta)