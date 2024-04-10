#Cores no Terminal

#padrao ansi compativel com python

print()

# \033[0;33;44m]  0=style, 33 tipo texto, 44 background

#style 0, 1, 4, 7 (melhores estilos para o python)
#0 none
#1 bold
#4 underline
#7 negative

#cores: 30 ao 37

#background: 40 ao 47

print(f'\033[0;30;41m Teste ') #letra branca, fundo vermelho
print('\033[m')
print(f'\033[4;33;44m Teste ') #Underline, letra branca, fundo azul
print('\033[m')
print(f'\033[1;35;43m Teste ') #Bold, letra azul, fundo amarelo
print('\033[m')
print(f'\033[30;42m Teste ') #padrao, letra vermelha, fundo verde
print('\033[m')
print('\033[m Teste ') #padrao
print(f'\033[7;30m Teste ') #inverso
print('\033[m')
print(f'\033[0;30;41m Teste \033[m')
print()

print(19//2)
print( 3 * 5 + 4 ** 2)
