#Exercício Python 038: 

#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os.
# mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

print()

num1 = int(input('Digite um numero inteiro: '))
num2 = int(input('Digite outro numero inteiro: '))

if num1 > num2:
      print('O primeiro valor é o maior')
else:
      print('O segundo valor é o maior')

if num1 == num2:
      print('Não existe valor maior, os dois são iguais')


print()