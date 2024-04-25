#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
#  O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre


print()

mais = total = 0
barato = ''
menor = 10000000000

print('---' * 15)
print(f'{"LOJA SUPER BARATÃO:":>32}')
print('---' * 15)
while True:
      produto = input('Nome do Produto: ')
      preco = int(input('Preço: R$ '))
      total += preco
      if preco > 1000:
            mais += 1
      if preco < menor:
            menor = preco
            barato = produto
      continuar = input('Quer continuar? [S/N]: ').strip().upper()
      if continuar in 'nN':
            break
print(f'{"-" * 10} FIM DO PROGRAMA {"-" * 10}')
print(f'Total da compra foi: R${total:.2f}')
print(f'Temos {mais} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa R$ {menor}')
print()