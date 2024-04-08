#26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

print()

nome = str(input('Digite um Nome: ')).strip().upper()

print(f'A letra A aparece {nome.count('A')} no seu nome. ') 
print(f'A primeira letra A apareceu na posição: {nome.find('A')+1 }') #+1 para nossa visao
print(f'A última letra A apareceu na posição: {nome.rfind('A')+1 }') #rfind para começar a contar da direita

print()