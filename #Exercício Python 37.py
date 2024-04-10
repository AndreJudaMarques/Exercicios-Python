#Exercício Python 37 

#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer 
#e peça para o usuário escolher qual será a base de conversão: 
#1 para binário, 2 para octal e 3 para hexadecimal.

print()

numero = int(input('Digite um numero inteiro: '))

print(f'Escolha uma das Bases para converter: ')
print(f'[ 1 ] converter para BINARIO')
print(f'[ 2 ] converter para OCTAL')
print(f'[ 3 ] converter para HEXADECIMAL')

opcao = int(input('Sua opção: '))

if opcao == 1:
      print(f'{numero} convertido para Binário e igual a {bin(numero)[2:]} ')
elif opcao == 2:
      print(f'{numero} convertido para Octal e igual a {oct(numero)[2:]} ')
elif opcao == 3:
      print(f'{numero} convertido para Hexadecimal e igual a {hex(numero)[2:]} ') #[2:] para nao aparecer os simbolos escolhidos
else:
      print('Opção inválida, tente novamente.')            

#bin(numero)
#oct(numero)
#hex(numero)

print()