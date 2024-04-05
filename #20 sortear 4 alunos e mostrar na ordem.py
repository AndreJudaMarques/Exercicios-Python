#20 sortear 4 alunos e mostrar na ordem


print()
print()

from random import shuffle

print('Sortear alunos e mostrar ordem')
print()

al = 1

alunos = []


while al < 5:
      aluno1 = input("Digite o nome do {}º aluno: ".format(al))
      alunos.append(aluno1)      
      al += 1

embaralhado = shuffle(alunos)

print(alunos)


print()
print()