#8 Faça um Programa que pergunte quanto você ganha por hora 
#e o número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês.

print()
print()

ganha = float(input('Quanto você ganha por hora? ')) #200
horas = int(input('Quantas horas trabalhadas por mes? ')) #20

salario = horas * ganha

print('O seu salário é de R${} por mês' .format(salario))

print()
print()