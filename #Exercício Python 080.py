#Exercício Python 080: Crie um programa onde o usuário possa digitar 
# cinco valores numéricos e cadastre-os em uma lista, 
# já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

print()

lista = []

for iten in range(0,5):
      num = int(input('Digite um valor: '))
      if iten == 0 or num > lista[-1]:
            lista.append(num)
            print('Adicionado ao final da lista...')
      else:
            pos = 0 #posicao 
            while pos < len(lista):
                  if num <= lista[pos]:
                        lista.insert(pos, num)
                        print(f'Adicionado na posicao {pos} da lista')
                        break
                  pos += 1


print('-=-' * 15)      
print(lista)
print()

# lista = []

# lista.append(5)
# lista.append(6)
# lista.insert(0,7)
# lista.append(8)
# print(lista)