#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.


print()

print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)

termo = int(input('Primeiro termo: '))

razao = int(input('Razão: '))

# cont = 0

# while cont < 10:                            ESTE FUI EU QUE FIZ
#       print(f'{termo}', end=' -> ')
#       termo = termo + razao
#       #print(f'{termo}', end='')
#       cont += 1
# print('ACABOU')

#RESOLVER COM FOR

decimo = termo + ( 10 - 1) * razao
for i in range(termo, decimo + razao, razao):        # ESTE COM AJUDA DA AULA
      print(f'{termo}', end=' -> ')
      termo = termo + razao
print('ACABOU')

print()

