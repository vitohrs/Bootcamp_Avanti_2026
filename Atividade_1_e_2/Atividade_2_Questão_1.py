# ATIVIDADE 2
# 1 QUESTÃO: Escreva uma função que receba uma lista de números e retorne outra lista com os números ímpares.

list = [1,2,3,4,5,6,7,8,9,10]
lista_impar = []
for x in list:
    if x % 2 == 1:
        lista_impar.append(x)
print(lista_impar)
