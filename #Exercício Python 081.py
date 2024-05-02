#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

print()

lista =[]

cont = 0
while True:
      n = int(input('Digite um valor: '))
      cont += 1
      lista.append(n)
      continuar = input('Quer continuar: [S/N]: ').lower().strip()
      if continuar == 'n':
            break
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
      print('O valor 5 está na lista')
else:
      print('O valor 5 não está na lista')

print()