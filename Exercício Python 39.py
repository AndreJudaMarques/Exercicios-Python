#Exercício Python 39: 

from datetime import date

print()

dataHoje = date.today()

anoHoje = date.today().year #2024

anoNascimento = int(input('Qual seu ano de nascimento? '))

idade =  anoHoje- anoNascimento

print(f'Quem nasceu em {anoNascimento} tem {idade} anos de idade em {anoHoje}')

if idade == 18:
      print(f'Você deve se alistar IMEDIATAMENTE! ')

elif idade > 18:
     print(f'Você já deveria ter se aliastado há {(idade - 18)} anos. ') 
     print(f'Seu alistamento foi em {anoHoje - (idade - 18)}')

elif idade < 18:
      print(f'Ainda faltam {(18-idade)} anos para o alistamento. ')
      print(f'Seu alistamento será em {anoHoje + (18-idade)}. ')

print()