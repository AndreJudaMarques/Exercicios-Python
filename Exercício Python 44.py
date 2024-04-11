# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto

# – à vista no cartão: 5% de desconto

# – em até 2x no cartão: preço formal 

# – 3x ou mais no cartão: 20% de juros

print()

valor = float(input('Qual o valor do produto: R$'))

print(f'''Qual opção de pagamento:
      \n[1] à vista dinheiro/cheque: 10% de desconto
      \n[2] à vista no cartão: 5% de desconto
      \n[3] em até 2x no cartão: preço formal
      \n[4] 3x ou mais no cartão: 20% de juros''')
print()
opcao = int(input('Opção: '))

if opcao == 1:
      print(f'Sua compra no valor de {valor:.2f} irá custar R${(valor - (valor * 0.1)):.2f} com 10% de desconto.')

elif opcao == 2:
      print(f'Sua compra no valor de {valor:.2f} irá custar R${(valor - (valor * 0.05)):.2f} com 5% de desconto.')

elif opcao == 3:
      print(f'Sua compra no valor de {valor:.2f} irá custar o mesmo valor de {valor} podendo parcelar em até 2x.')

elif opcao == 4:
      print(f'Sua compra no valor de {valor:.2f} irá custar R${(valor + (valor * 0.2)):.2f} com 20% de juros podendo parcelar em até 3x.')

else:
      print(f'Opção inválida, tente novamente.')

print()