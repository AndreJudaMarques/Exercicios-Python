# #Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#  Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

print()

palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar',
            'Trabalhar', 'Mercado', 'Programador', 'Futuro')

for palavra in palavras:
      print(f'\nNa palavra {palavra.upper()} temos:', end=' ')
      for letra in palavra:
            if letra in 'aeiouAEIOU':
                  print(letra.lower(), end=' ')

print()
print()