#Exercício Python 107

print()

import moedas

preco = float(input('Digite o preço: R$'))
print(f'A metade de R${preco:.2f} é de R${moedas.metade(preco)} ')
print(f'O dobro de R${preco:.2f} é de R${moedas.dobro(preco)}')
print(f'Aumentando 10% temos {moedas.aumentar(preco)}')

print()