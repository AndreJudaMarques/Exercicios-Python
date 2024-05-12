#Exercício Python 098

print()

def linha():
      print('-=-' * 12)

def cont1():
      cont = 1
      while cont < 10:
            print(cont, end=' ')
            cont += 1
      print('FIM!')

def contm1():
      cont = 10
      while cont >= 0:
            print(cont, end=' ')
            cont -= 2
      print('FIM!')

def contador():
      """
      ->faz uma contagem e mostra na tela
      com os respectivos inputs

      ini: inicio da contagem
      fim: fim da contagem
      passo: passos da contaggem
      return: sem retorno
      """
      if ini <= fim:
            cont = ini
            while cont < fim:
                  print(cont, end=' ')
                  cont += passo
            print(cont, end=' ')
            print('FIM!')
      else:
            if ini >= fim:
                  cont = ini
            while cont > fim:
                  print(cont, end=' ')
                  cont += passo
            if cont == fim:
                  print(cont, end=' ')
            print('FIM!')
      print()
      

linha()
print('Contagem de 1 até 10 de 1 em 1:')
cont1()
linha()
print('Contagem de 10 até 0 de 2 em 2:')
contm1()
linha()
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('passo: '))
linha()
print(f'Contagem de {ini} até {fim} de {passo} em {passo}:')
contador()

print()

help(contador)