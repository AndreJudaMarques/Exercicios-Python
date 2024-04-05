#9 Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

print()
print()

temp = float(input('Qual a temperatura em Fº? '))

cel = 5 *((temp - 32) /9)

print('A temperatura {}Fº convertida é de {}Cº. '.format(temp, cel))

print()
print()
