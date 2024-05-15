from lib.interface import *
import os

def criarArquivo(nome):
      try:
           a = open(nome, 'wt+')
           a.close()
      except:
           print('houve erro')
      else:
           print(f'Arquivo {nome} criado com sucesso')

    

def lerArquivo(nome):
      try:
          a = open(nome, 'rt')
      except:
           print('Houve erro')
      else:
           cabecalho('PESSOAS CADSTRADAS')
           print(a.readline())


'''def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
        return True
    except FileNotFoundError:
        return False'''