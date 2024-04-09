#Exercício Python 33: Faça um programa que leia três números
# e mostre qual é o maior e qual é o menor.

print()

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
num3 = int(input('Terceiro valor: '))

if num1 < num2 & num3: #poderia ser if num1 < num2 and num1 < num3
      print(f'O menor valor digitado foi {num1}')
else:
      if num2 < num1 & num3:
            print(f'O menor valor digitado foi {num2}')

      elif num3 < num1 & num2:
            print(f'O menor valor digitado foi {num3}')

if num1 > num2 & num3:
      print(f'O maior valor digitado foi {num1}')
else:
      if num2 > num1 & num3:
            print(f'O maior valor digitado foi {num2}')

      elif num3 > num1 & num2:
            print(f'O maior valor digitado foi {num3}')


print()

#'O menor valor digitado foi {}'
