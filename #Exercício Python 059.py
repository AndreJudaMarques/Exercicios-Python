#Exercício Python 059

# tela:

# [ 1 ] somar

# [ 2 ] multiplicar

# [ 3 ] maior

# [ 4 ] novos números

# [ 5 ] sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

print()

numero1 = float(input('Digite o primeiro valor: '))
numero2 = float(input('Digite o segundo valor: '))

print('   [1] somar')
print('   [2] multiplicar')
print('   [3] maior')
print('   [4] novos números')
print('   [5] sair do programa')

op = int(input('>>>> Qual sua opção? '))

while op != 5:
      if op == 1:
            print(f'A soma entre {numero1} + {numero2} é: {numero1 + numero2:.1f}')
            print('=-=' * 15)
            sleep(1)
            print('   [1] somar')
            print('   [2] multiplicar')
            print('   [3] maior')
            print('   [4] novos números')
            print('   [5] sair do programa')
            op = int(input('>>>> Qual sua opção? '))
      
      if op == 2:
            print(f'A multiplicação entre {numero1} x {numero2} é: {numero1 * numero2:.1f}')
            print('=-=' * 15)
            sleep(1)
            print('   [1] somar')
            print('   [2] multiplicar')
            print('   [3] maior')
            print('   [4] novos números')
            print('   [5] sair do programa')
            op = int(input('>>>> Qual sua opção? '))
      
      if op == 3:
            if numero1 > numero2:
                  print(f'O maior entre {numero1} e {numero2} é: {numero1:.1f}')
            else:
                  print(f'O maior entre {numero1} e {numero2} é: {numero2:.1f}')
            print('=-=' * 15)
            sleep(1)
            print('   [1] somar')
            print('   [2] multiplicar')
            print('   [3] maior')
            print('   [4] novos números')
            print('   [5] sair do programa')
            op = int(input('>>>> Qual sua opção? '))
      
      if op == 4:
            numero1 = float(input('Digite o primeiro valor: '))
            numero2 = float(input('Digite o segundo valor: '))
            print('=-=' * 15)
            sleep(1)
            print('   [1] somar')
            print('   [2] multiplicar')
            print('   [3] maior')
            print('   [4] novos números')
            print('   [5] sair do programa')
            op = int(input('>>>> Qual sua opção? '))
      
      if op > 5:
            print('Opção inválida. Tente novamente.')
            print('=-=' * 15)
            sleep(1)
            print('   [1] somar')
            print('   [2] multiplicar')
            print('   [3] maior')
            print('   [4] novos números')
            print('   [5] sair do programa')
            op = int(input('>>>> Qual sua opção? '))
            
print('Finalizando...')
sleep(1)
print('Fim do programa! Volte sempre.')

print()