#Exercício Python 083

print()

exp = input('Digite a expressão: ')

dir = []
esq = []

for i in exp:
      if i == "(":
            esq.append(i)
      if i == ")":
            dir.append(i)

if len(dir) == len(esq):
      print('Sua expressao está correta!')
else:
      print('Sua expressao está errada!')

print()
print()

#((a+b)*c)(x+y(3+2/3)*z)
#((((a+b)*c)+2)/4))