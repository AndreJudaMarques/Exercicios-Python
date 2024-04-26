#Exercício Python 72: Crie um programa que tenha uma dupla totalmente
#  preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

print()

numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'desesseis', 'desessete', 'dezoito',
           'dezenove', 'vinte')

n = int(input('Digite um número entre 0 e 20: '))

while 0 < n > 20:
      n = int(input('Digite um número entre 0 e 20: '))

print(f'Você digitou o número "5{numeros[n]}"')





print()
