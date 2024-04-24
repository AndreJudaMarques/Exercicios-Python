#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores
# lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

print()

numero = int(input('Digite um número: '))

continuar = input('Quer continuar? [S/N]: ').lower().strip()

total = numero
maior = menor = numero
cont = 1
while continuar != 'n':
      numero = int(input('Digite um número: '))
      cont += 1
      total = total + numero
      if numero > maior:
            maior = numero
      elif numero < menor:
            menor = numero
      continuar = input('Quer continuar? [S/N]: ').lower().strip()
      
print(f'Você digitou {cont} números e a média foi {total / cont}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
print()