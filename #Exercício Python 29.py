#Exercício Python 29: 
#Escreva um programa que leia a velocidade de um carro. 
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

print()

velocidade = int(input('Qual a velocidade capturada do carro? '))

multa = (velocidade - 80) * 7

if velocidade > 80:
      print('MULTADO! Você exedeu o limite permitido que é de 80km/h')
      print(f'Você deve pagar uma multa de R${multa}! ')
else:
      print('Tenha um bom dia! Dirija com segurança! ')
      

print()