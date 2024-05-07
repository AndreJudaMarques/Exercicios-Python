#Exercício Python 089

print()

todos = []
lista = []
notas = []
todasnotas = []

while True:
      nome = input('Nome: ')
      nota1 = float(input('Nota 1: '))
      notas.append(nota1)
      nota2 = float(input('Nota 2: '))
      notas.append(nota2)
      media = (nota1 + nota2) / 2
      todasnotas.append(notas[:])
      notas.clear()
      lista.append(nome)
      lista.append(media)
      todos.append(lista[:])
      lista.clear()
      media = 0
      continuar = input('Quer continuar ? [S/N]: ').lower()
      if continuar in 'nN':
            break

print('-=-' * 30)
print(f'{'Nº':<} {'NOME':^10} {'MEDIA':>20}')
print('---' * 30)

for i, l in enumerate(todos):
      print(f'{i} {l[0]:^12} {l[1]:>20} ')

while True:
      n = int(input('Mostrar as notas de qual aluno? [999 PARAR]: '))
      if n == 999:
            break
      else:
            print(f'Notas de {todos[n][0]} são {todasnotas[n]}')
            print('---' * 20)

print()
print('FINALIANDO...')
print('<<< VOLTE SEMPRE >>>')
print()
