def leiaint(msg):
      valor = 0
      while True:
            n = input(msg).strip()
            if n.isnumeric():
                  valor = int(n)
                  break
            else:
                  print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
      return valor


def linha(tam=42):
      return '-' * tam


def cabecalho(txt):
      print(linha())
      print(txt.center(42))
      print(linha())


def menu(lista):
      cabecalho('MENU PRINCIPAL')
      c = 1
      for item in lista:
            print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
            c+=1
      print(linha())
      opc = leiaint('Sua Opção: ')
      return opc

