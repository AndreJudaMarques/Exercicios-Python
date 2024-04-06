#22: Crie um programa que leia o nome completo de uma pessoa e mostre:

# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

# – O nome com todas as letras maiúsculas e minúsculas.

# – Quantas letras ao todo (sem considerar espaços).

# – Quantas letras tem o primeiro nome.

print()

nome = input('Digite seu nome completo:  ').strip() # strip para cortar os espaços

print('{}   Nome normal -' .format(nome))
print('{}   Tudo maiuscula -' .format(nome.upper()))
print('{}   Tudo minuscula -' .format(nome.lower()))
print('{}   Quantidade de letras ao todo -' .format(len(nome) - nome.count(' ')))
print('{}   Quantidade de letras do primeiro nome' .format(nome.find(' '))) #find acha a posicao do primeiro espaço, determinado pelo (' ')


print()
print()