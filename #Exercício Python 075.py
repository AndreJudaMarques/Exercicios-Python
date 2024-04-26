#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado 
# e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.

# B) Em que posição foi digitado o primeiro valor 3.

# C) Quais foram os números pares.

print()

#n = []

n = (int(input("Digite um numero: ")), int(input("Digite outro numero: ")), 
      int(input("Digite mais um numero: ")), int(input('Digite um ultimo numero: ')))

print(f'Você digitou os valores: {n}')
print(f'O Valor 9 apareceu {n.count(9)}')
print(f'O Valor 3 apareceu na {n.index(3)+1}º posição')
pares = []
for i in n:
      if i % 2 == 0:
            pares.append(i)
print(f'Os valores pares digitados foram {pares}')


print()