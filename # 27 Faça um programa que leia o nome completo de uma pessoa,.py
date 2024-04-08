#Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, 
#mostrando em seguida o primeiro e o último nome separadamente

print()

nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split() # divide em espacos e faz uma lista de cada

print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {n[0]}')
print(f'Seu ultimo nome é {n[len(n)-1]}') #Conta quantas divisoes splits e mostra a ultima(-1)


print()

