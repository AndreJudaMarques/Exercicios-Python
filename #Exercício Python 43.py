# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
#calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

# – IMC abaixo de 18,5: Abaixo do Peso

# – Entre 18,5 e 25: Peso Ideal

# – 25 até 30: Sobrepeso

# – 30 até 40: Obesidade

# – Acima de 40: Obesidade Mórbida

print()

peso = float(input('Qual seu peso atual? (Kg) '))

altura = float(input('Qual sua altura? (m) '))

# IMC = peso / (altura x altura).
#  kg/m2. Resultado

imc = peso / (altura * altura)

if imc < 18.5:
      print(f'O IMC dessa pessoa é de {imc:.2f}')
      print(f'Você está abaixo do peso.')

elif 18.5 < imc < 25:
      print(f'O IMC dessa pessoa é de {imc:.2f}')
      print(f'Essa pessoa está com peso ideal.')

elif 25 < imc < 30:
      print(f'O IMC dessa pessoa é de {imc:.2f}')
      print(f'Essa pessoa está com Sobrepeso.')

elif 30 < imc < 40:
      print(f'O IMC dessa pessoa é de {imc:.2f}')
      print(f'Essa pessoa está com Obesidade.')

elif imc < 40:
      print(f'O IMC dessa pessoa é de {imc:.2f}')
      print(f'Essa pessoa está com Obesidade Mórbida.')

print()
