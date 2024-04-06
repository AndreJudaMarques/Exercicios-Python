#23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#mostrar numero, unidade, dezena, centena, milhar

print()

num = int(input('Digite um numero entre 0 e 9999: '))
n = str(num)
u = num // 1 % 10 #divisao por 1 e o resto da divisa por 10 pra pegar o ultimo numero
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('O numero digitado foi o: {}' .format(num))
print('A unidade é {} ' .format(u))
print('A dezena é {} ' .format(d))
print('A centena é {} ' .format(c))
print('O milhar é {} ' .format(m))
print('O {} possui {} números ' .format(num, len(n)))








print()
print()