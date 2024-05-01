#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos 
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

print()

lista = []

while True:
      num = int(input('Digite um valor: '))
      if num not in lista:
            lista.append(num)
            print('Valor adicionado com sucesso...')
      else:
            print('Valor duplicado! Não vou adicionar.')
      continuar = input('Quer continuar: [S/N] ').lower().strip()
      if continuar == "n":
            break
print('-=-' * 15)
print(sorted(lista))
print()