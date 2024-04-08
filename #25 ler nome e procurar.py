#Exercício Python 25: 
#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

print()

nome = str(input('Qual seu nome completo: ')).strip().lower()

print(f'Seu nome tem Silva? {'silva' in nome}')

print()