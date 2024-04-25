#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
#  A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:

# A) quantas pessoas tem mais de 18 anos.

# B) quantos homens foram cadastrados.

# C) quantas mulheres tem menos de 20 anos.

print()

maiores = 0
menos = 0
homens = []
while True:
      print('---' * 15)
      print(f'{"CADASTRE UMA PESSOA:":>32}')
      print('---' * 15)
      idade = int(input('Idade: '))
      if idade > 18:
            maiores += 1
      sexo = input('Sexo [M/F]: ').strip().upper()
      if sexo in 'mM':
            homens.append(sexo)
      if sexo in 'fF' and idade < 20:
            menos += 1
      continuar = input('Quer continuar? [S/N]: ').strip().upper()
      if continuar in 'nN':
            break
print('---' * 15)
print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Ao todo temos {len(homens)} homens cadastrados')
print(f'E temos {menos} mulheres com menos de 20 anos')
print()