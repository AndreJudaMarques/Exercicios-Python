#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos
#  e seus respectivos preços, na sequência. No final, mostre uma listagem de preços,
# organizando os dados em forma tabular.

print()

print('---' * 15)
print(f'{"Listagem de Preços":^40}')
print('---' * 15)

produtos = ('Lapis', 1.75,
            'Borracha', 2,
            'Caderno', 15.9,
            'Estojo', 25,
            'Transferidor', 4.2,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.3,
            'Livro', 34.9)

for posicao in range(0, len(produtos)):
      if posicao % 2 == 0:
            print(f'{produtos[posicao]:.<30}', end='')
      else:
            print(f'R${produtos[posicao]:>7.2f}')
print('---' * 15)
print()