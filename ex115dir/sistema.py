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
            lerArquivo(arq)
      elif resposta == 2:
            #cadsatrar nova pessoa
            cabecalho('NOVO CADASTRO') 
            nome = str(input('Nome: '))
            idade = leiaint('Idade: ')
            cadastrar(arq, nome, idade)
      elif resposta == 3:
            cabecalho('Saindo do sistema... Até logo!')
            break
      else:
            print('\033[31mERRO! Digite uma opção válida!\033[m')
            sleep(1.5)

print()  