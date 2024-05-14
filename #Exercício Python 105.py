#Exercício Python 105

print()

def notas():
      dici = {}
      lista = ['Kaka', 1, 2]
      dados = []
      while True:
            lista.clear()
            nome = input('nome do aluno: ')
            lista.append(nome)
            n1 = float(input('Nota 1: '))
            lista.append(n1)
            n2 = float(input('Nota 2: '))
            lista.append(n2)
            dados.append(lista)
            resp = input('Deseja continuar? [P= PARAR/ C=CONTINUAR]: ').upper()
            if resp == 'P':
                  break
      #dici['Quantidade de notas'] = lista
      print(lista)
      print(dici)
      print(dados)


notas()

print('')