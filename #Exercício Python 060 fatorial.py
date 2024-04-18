#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. 
# Exemplo:
# 5! = 5 x 4 = 20
# 20 x 3 = 60
# 60 x 2 = 120
#x 1 = 120


print()

numero = int(input('Digite um número!: '))

resultado = 1

while numero > 1:
      resultado = resultado * numero
      numero -= 1

print(resultado)


      


