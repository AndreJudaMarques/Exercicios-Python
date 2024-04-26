#Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados 
# da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

# a) Os 5 primeiros times.

# b) Os últimos 4 colocados.

# c) Times em ordem alfabética.

# d) Em que posição está o time da Chapecoense.

print()

times = ( "Flamengo", "Palmeiras", "Santos", "São Paulo", "Corinthians", "Grêmio",
                  "Internacional", "Atlético Mineiro", "Cruzeiro", "Fluminense", "Botafogo",
                  "Vasco da Gama", "Bahia", "Sport", "Coritiba", "Athletico Paranaense",
                  "Fortaleza", "Ceará", "Goiás", "Chapecoense")

print('-=-' * 50)
print(times)
print('-=-' * 50)
print(f'Os 5 primeiros times são {times[:5]}')
print('-=-' * 50)
print(f'Os últimos 4 colocados são {times[-4:]}')
print('-=-' * 50)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=-' * 50)
print(f'O Chapecoense está na {times.index('Chapecoense')+1}º posição')
print('-=-' * 50)
print(f'{len(times)}')


print()


print()