#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa,
#  mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado,
# peça a digitação novamente até ter um valor correto.


print()

sexo = input('Qual seu sexo ? "M" ou "F": ').upper().strip()[0]

while sexo not in 'mMfF':
      sexo = input('Dados inválidos. Informe o sexo novamente: ')

print(f'Sexo "{sexo.upper()}" registrado com sucesso')

print()