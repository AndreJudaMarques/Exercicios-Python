#Exercício Python 040: Crie um programa que leia duas notas de um aluno

# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

print()

nota1 =  float(input('Digite a primeira nota: '))
nota2 =  float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
      print(f'Média {media:.1f}; REPROVADO! ')

elif 7 > media >= 5:
       print(f'Média {media:.1f}; RECUPERAÇÃO! ')

elif media >= 7:
      print(f'Média {media:.1f}; APROVADO! ')

print()