from lib.interface import *

print()

while True:
      resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do sistema'])
      if resposta == 1:
            print('Opção 1')
      elif resposta == 2:
            print('Opção 2') 
      elif resposta == 3:
            print('Opção 3')
            break
      else:
            print('ERRO! Digite uma opção válida!')

print()  ######### 14:47 minutos