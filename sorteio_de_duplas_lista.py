"""
Crie um programa que sorteie uma dupla e mostre na tela.

Exemplo do sorteio:
'Aluno3 Aluno6'

'Aluno2 Aluno5'

'Aluno1 Aluno4'
"""
from random import shuffle

lista1 = ['Aluno1', 'Aluno2', 'Aluno3']
lista2 = ['Aluno4', 'Aluno5', 'Aluno6']
shuffle(lista1)
shuffle(lista2)
for p1, p2 in zip(lista1, lista2):
    print(p1, p2)

