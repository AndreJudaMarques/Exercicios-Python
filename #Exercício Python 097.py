#Exercício Python 097

print()


def linha(txt):
      simb = 0
      while simb < len(txt):
            print('~', end='')
            simb += 1
      print('~' * 4, end='')
      print()

def mensagem(texto):
      linha(texto)
      print(f'  {texto}')
      linha(texto)

mensagem('Gustavo Guanabara')
mensagem('curso em video')
mensagem('Curso de Python no Youtube')
mensagem('CeV')

print()