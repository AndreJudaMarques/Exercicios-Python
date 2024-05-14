def aumentar(n):
      dez = n*0.1
      return n + dez

def metade(n):
      return n / 2

def dobro(n):
      return n * 2

def resumo(n, aum=0, red=0):
      print('-' * 35)
      print('          Resumo do Valor    ')
      print('-' * 35)
      print(f'Preço analisado:       R${n:.2f}')
      print(f"Dobro do preço:        R${dobro(n):.2f}")
      print(f'Metade do preço        R${metade(n):.2f}')
      print(f'{aum}% de aumento:        R${(n + ((n)*aum) / 100):.2f}')
      print(f'{red}% de redução:        R${(n - ((n)*red) / 100):.2f}')
      print('-' * 35)