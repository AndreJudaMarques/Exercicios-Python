#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#  No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.

print()

idades = []
soma = 0
velho = ''
maisVelho = 0
menos20 = 0

for pessoa in range(1,5):
      print('-' * 25)
      nome = input(f'Qual nome da {pessoa}º pessoa? ')
      idade = int(input('Qual a sua idade? '))
      soma = soma + idade
      media = soma / 4
      idades.append(idade)
      sexo = input('De qual sexo? "M" ou "F" ').upper()
      if sexo == "M":
            if idade > maisVelho:
                  maisVelho = idade
                  velho = nome
      elif sexo == "F":
            if idade < 20:
                  menos20 += 1

print()
print(f'A média das idades é de: {media:.1f} anos')
print(f'O homem mais velho tem {maisVelho} anos e se chama {velho}')
print(f'Existem {menos20} mulheres com menos de 20 anos')

print()

#fiz de primeira 