##Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário 
#e calcule o valor do seu aumento. 
#Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

print()

salario = float(input('Digite o seu salário: '))

dezP = (salario * 0.1) + salario
quinP = (salario * 0.15) + salario

if salario > 1250:
      print(f'Seu salário com aumento de 10% é de: R${dezP:.2f}')

else:
      print(f'Seu salário com aumento de 15% é de: R${quinP:.2f}')

print()

