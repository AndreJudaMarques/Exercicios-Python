#19 ler 4 alunos sortear 1

print()
print()

import random

print('Sortear alunos!')
print()

aluno1 = input('Digite o nome do 1 aluno:')
aluno2 = input('Digite o nome do 2 aluno:')
aluno3 = input('Digite o nome do 3 aluno:')
aluno4 = input('Digite o nome do 4 aluno:')
print()

Rand = random.randint(1,4)

if Rand == 1:
      print('O aluno escolhido foi o {}. '.format(aluno1))
if Rand == 2:
      print('O aluno escolhido foi o {}. '.format(aluno2))
if Rand == 3:
      print('O aluno escolhido foi o {}. '.format(aluno3))
if Rand == 4:
      print('O aluno escolhido foi o {}. '.format(aluno4))


print()
print()