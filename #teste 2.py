#teste 2

dados = {}
galera = [{'nome': 'Kaka', 'gols': [3]}, {'nome': 'Vampeta', 'gols': [5]}]

gol = [5]

dados['gols'] = gol

galera[1]['gols'] = dados['gols']


print(galera)
print(gol)
print(dados)
print(galera[1]['nome'])