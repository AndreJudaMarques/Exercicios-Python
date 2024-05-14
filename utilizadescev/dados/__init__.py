

def leiadinheiro(msg):
      valido = False
      while not valido:
            entrada = str(input(msg)).replace(',','.').strip()
            if entrada.isalpha() or entrada == '':
                  print(f'\033[0;31mERRO: preço inválido\033[m')
            else:
                  valido = True
                  return float(entrada)
            

def leiaint(msg):
      valor = 0
      while True:
            n = input(msg)
            if n.isnumeric():
                  valor = int(n)
                  break
            else:
                  print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
      return valor