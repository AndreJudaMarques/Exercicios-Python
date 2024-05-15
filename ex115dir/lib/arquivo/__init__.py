from lib.interface import *
import os
from time import sleep

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
            for linha in arquivo:
                dado = linha.split(';')
                dado[1] = dado[1].replace('\n', '')
                print(f'{dado[0]:<30} {dado[1]:>3} anos')
    except Exception as e:
        print(f'Houve um erro ao ler o arquivo: {e}')
      
    '''finally:
        a.close()'''


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        caminho = os.path.join('ex115dir', 'lib', 'arquivo', arq)
        with open(caminho, 'at') as arquivo:
            arquivo.write(f'{nome};{idade}\n')
        print(f'Novo registro de {nome} adicionado')
        sleep(1)
    except Exception as e:
        print(f'Houve um erro ao cadastrar o registro: {e}')


'''def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
        return True
    except FileNotFoundError:
        return False'''