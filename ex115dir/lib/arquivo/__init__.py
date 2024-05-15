from lib.interface import *
import os

def criarArquivo(nome):
      try:
           caminho = os.path.join('ex115dir', 'lib', 'arquivo', nome)
           with open(caminho, 'wt+'):
            pass
      except:
           print('houve erro')
      else:
           print(f'Arquivo {nome} criado com sucesso')

    

def lerArquivo(nome):
    try:
        caminho = os.path.join('ex115dir', 'lib', 'arquivo', nome)
        with open(caminho, 'rt') as arquivo:
            cabecalho('PESSOAS CADASTRADAS')
            print(arquivo.read())
    except Exception as e:
        print(f'Houve um erro ao ler o arquivo: {e}')


'''def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
        return True
    except FileNotFoundError:
        return False'''