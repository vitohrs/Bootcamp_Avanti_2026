# ATIVIDADE 2
# 4 QUESTÃO: Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor na lista.

lista = [1, 3, 5, 7, 8, 9, 32, 33]

MaiorNumero = max(lista)

copiaLista = lista.copy()

copiaLista.remove(MaiorNumero)

segundoMaior = max(copiaLista)

print(segundoMaior)