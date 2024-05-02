#Exercício Python 082:

print() 

lista = []
pares = []
impares = []

while True:
      n = int(input('Digite um numero: '))
      lista.append(n)
      if n % 2 == 0:
            pares.append(n)
      else:
            impares.append(n)
      continuar = input('Quer continuar [N/S]: ').lower()
      if continuar == 'n':
            break

print(f'A lista completa é {lista}') 
print(f'A lista de pares é {pares}') 
print(f'A lista de impares é {impares}') 

print() 