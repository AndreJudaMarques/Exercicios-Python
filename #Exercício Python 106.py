#Exercício Python 106

print()

def miniSis():
      from time import sleep

      def linha():
            print('~' * 27)

      while True:
            print("\033[42m", end="")
            linha()
            print('  Sistema de ajuda PyHelp')
            linha()
            print("\033[0m")
            nome = input('Função ou Biblioteca? :> ').lower()
            if nome == 'fim':
                  break   
            else:
                  print("\033[44m", end="")  # zul
                  linha()
                  print(f"Acessando o manual do comando '{nome}'")
                  linha()
                  sleep(1)
                  print("\033[0m", end="")  # Resetar a cor de fundo
                  print("\033[47m\033[30m", end="")  # Fundo branco, texto preto
                  help(nome)
                  print("\033[0m")
      print("\033[46m", end="")
      print('  FIM  ')
      print("\033[0m")

miniSis()

#help(len)

print()