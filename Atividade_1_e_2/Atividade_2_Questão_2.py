# ATIVIDADE 2
# 2 QUESTÃO: Escreva uma função que receba uma lista de números e retorne outra lista com os números primos presentes.

list = [1,2,3,4,5,6,7,8,9,10]
lista_primos = []

for x in list:
    divisores = 0

    for i in range (1, x+1):
        if x % i == 0:
            divisores += 1

    if divisores == 2:
        lista_primos.append(x)

print(lista_primos)