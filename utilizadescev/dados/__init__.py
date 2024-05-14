

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
            n = input(msg).strip()
            if n.isnumeric():
                  valor = int(n)
                  break
            else:
                  print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
      return valor

def leiareal(msg):
      while True:
        n = input(msg).strip().replace(',', '.')  # Substitui ',' por '.' para aceitar tanto ',' quanto '.' como separador decimal
        if not n.replace('.', '', 1).isdigit():  # Verifica se a string contém apenas dígitos e, no máximo, um ponto decimal
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
        else:
            return float(n)  # Converte e retorna a entrada como um número real
            
      return valor
