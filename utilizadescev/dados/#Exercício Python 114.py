#Exercício Python 114


import urllib.request
import ssl

print()

try:
    # Desativa a verificação de certificado SSL
    site = urllib.request.urlopen('https://www.pudim.com.br/', context=ssl._create_unverified_context())
    print('Tudo ok')
except Exception as e:
    print('Deu erro:', e)
    try:
        # Tentativa de tratamento do erro durante a exceção original
      raise e
    except Exception as inner_e:
        print('Erro durante tratamento da exceção original:', inner_e)  