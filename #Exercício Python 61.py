#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
#mostrando os 10 primeiros termos da progressão usando a estrutura while.

print()

print('Gerador de PA')
print('-=-' * 10)

termo = int(input('Qual primeiro termo: '))
razao = int(input('Qual razão da PA: '))

resultado = 0
pa = termo + razao # 7/ 
cont = 1
print(f'{termo}', end=' -> ')
print(f'{pa}', end=' -> ')
while cont < 9:
      resultado = pa + razao # 12/ 
      print(f'{resultado}', end=' -> ')
      pa = resultado
      cont += 1

print('FIM')
print()