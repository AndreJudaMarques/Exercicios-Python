#Exercício Python 66: Crie um programa que leia números inteiros pelo teclado.
#  O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas
# (desconsiderando o flag).

print()

n = soma = cont = 0

while cont > -1: #while true:
      n = int(input('Digite um valor: [999 para parar] : '))
      if n == 999:
            break
      else:
            cont += 1
            soma += n

print(f'A soma dos {cont} valores foi {soma}')

print()


# n = 0
# soma = 0
# cont = 0

# while n != 999:
#       n = int(input('Digite um valor: '))
#       cont += 1
#       soma += n

# print(soma-999)