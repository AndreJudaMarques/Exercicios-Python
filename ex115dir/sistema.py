from lib.interface import *

from lib.arquivo import *

from time import sleep

arq = 'cursoemvideo.txt'

#criarArquivo(arq)

print()

while True:
      resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do sistema'])
      if resposta == 1:
            #opcao de listar o conteudo de um arquivo
            cabecalho('Opção 1')
            lerArquivo(arq)
      elif resposta == 2:
            cabecalho('Opção 2') 
      elif resposta == 3:
            cabecalho('Saindo do sistema... Até logo!')
            break
      else:
            print('\033[31mERRO! Digite uma opção válida!\033[m')
            sleep(1.5)

print()  