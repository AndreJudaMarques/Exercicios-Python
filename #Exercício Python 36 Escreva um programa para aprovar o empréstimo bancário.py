#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário 

# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.


print()

valorDaCasa = int(input('Qual valor da casa: R$'))

salarioDoComprador = int(input('Qual salário do comprador: R$'))

quantosAnos = int(input('Quantos anos de financiamento? '))

# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

prestacao = (valorDaCasa / quantosAnos) / 12

trinta = salarioDoComprador * 0.3

if prestacao > trinta:
      print(f'Para pagar uma casa de R${valorDaCasa:.2f} em {quantosAnos} anos a prestação será de R${prestacao:.2f} ')
      print(f'Empréstimo \033[0;30;41m NEGADO! \033[m')
else:
      print(f'Para pagar uma casa de R${valorDaCasa:.2f} em {quantosAnos} anos a prestação será de R${prestacao:.2f} ')
      print(f'Empréstimo \033[1;35;43m APROVADO! \033[m')


print()