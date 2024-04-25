#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
#  No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
# e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print()

print('=' * 35)
print(f'{"Banco de Pobre":^36}')
print('=' * 35)

valor = int(input('Qual Valor voce quer sacar? R$ '))

contTotal = cont1 = cont10 = cont20 = cont50 = 0

while contTotal != valor:
      cont50 += 1
      contTotal += 50
      if contTotal >= valor:
            break

if contTotal == valor:
      contTotal = valor
else:
      contTotal -= 50
      cont50 -= 1

while contTotal != valor:
      cont20 += 1
      contTotal += 20
      if contTotal >= valor:
            break
            
if contTotal == valor:
      contTotal = valor
else:
      contTotal -= 20
      cont20 -= 1  

while contTotal != valor:
      cont10 += 1
      contTotal += 10
      if contTotal > valor:
            break            

if contTotal == valor:
      contTotal = valor
else:
      contTotal -= 10  
      cont10 -= 1

while contTotal != valor:
      cont1 += 1
      contTotal += 1
      if contTotal > valor:
            break          

if cont50 > 0:
      print(f'Total de {cont50} cédulas de R$50')

if cont20 > 0:
      print(f'Total de {cont20} cédulas de R$20')

if cont10 > 0:
      print(f'Total de {cont10} cédulas de R$10')

if cont1 > 0:
      print(f'Total de {cont1} cédulas de R$1')
print('=' * 35)
print('Volte sempe ao Banco de Pobre! Tenha um bom dia!')

print()