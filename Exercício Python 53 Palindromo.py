#Exercício Python 53:
# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
# desconsiderando os espaços. Exemplos de palíndromos:

print()

frase = str(input('Digite uma frase: ')).upper().strip()

palavras = frase.split()

junto = ''.join(palavras)

inverso = ''  #inverso = junto[::-1]     SOLUÇÃO SEM FOR, POREM A AULA É DE FOR

for letra in range(len(junto) -1, -1, -1): #pega o numero de letras menos 1, vai até a antes da primeira, voltando uma letra
      inverso += junto[letra]

print(f'O inverso de {junto} é {inverso} ')
if inverso == junto:
      print('Temos uma Palíndromo. ')
else:
      print('A frase digitada não é um Palíndromo.')


print()