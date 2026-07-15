# ATIVIDADE 2
# 3 QUESTÃO: Escreva uma função que receba duas listas e retorne outra lista com os elementos que estão presentes em apenas uma das listas.

lista1 = [1, 3, 5, 7, 8, 9, 32, 33]
lista2 = [2, 4, 6, 7, 8, 9, 33]


def funcao_lista(lista1, lista2):
    novalista = lista1.copy()
    contador = 0

    for x in lista2:
        contador = 0
        for i in novalista:
            if x == i:
                contador += 1
        if contador > 0:
            novalista.remove(x)
        else:
            novalista.append(x)

    return novalista
print(funcao_lista(lista1, lista2))