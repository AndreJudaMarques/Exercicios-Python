#Exercício Python 094

print()

galera = [] #lista
dados = {} #dicionario

soma = media = 0
while True:
      dados.clear()
      dados['nome'] = nome = input('Nome: ')
      while True:
            dados['sexo'] = sexo = input('Sexo: [M/F]: ').upper()[0]
            if dados['sexo'] in 'MF':
                  break
            print('ERRO! Responda apenas M ou F.')
      dados['idade'] = idade = int(input('Idade: '))
      soma += dados['idade']
      galera.append(dados.copy())
      while True:
            resp = input('Quer continuar? [S/N]: ').upper()[0]
            if resp in 'SN':
                  break
            print('ERRO! Responda apenas S ou N.')      
      if resp == 'N':
            break
print('-=-' * 15) # até aqui é a leitura dos dados, abaixo sao os resultados
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos')
print(f'C) As Mulheres cadastradas foram ', end='')
for p in galera:
      if p['sexo'] == 'F':
            print(f'{p["nome"]} ', end='')
print()
print(f'D) Lista de pessoas acima da média: ', end='')
for p in galera:
      if p["idade"] >= media:
            print(f'{p["nome"]} ', end='')
print()
print('<< ENCERRADO>>')
print()