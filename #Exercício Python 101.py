#Exercício Python 101

from datetime import date

print()

print('--' * 10)

def voto(n):
      anoHoje = date.today().year
      
      idade = anoHoje - n
      
      if 70 > idade > 18:
            print(f'Com {idade} anos: VOTO OBRIGATÓRIO. ')

      if idade >= 70:
            print(f'Com {idade} anos: VOTO OPCIONAL. ')

      if idade < 18:
            print(f'Com {idade} anos: NÃO VOTA. ')      
      return idade


anoNasci = int(input('Em que ano você nasceu? '))
print(voto(anoNasci))

print()