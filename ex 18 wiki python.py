#ex 18

#Faça um programa que peça o tamanho de um arquivo para download (em MB) 
#e a velocidade de um link de Internet (em Mbps), 
#calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

# 1 MB = 8 Mbps

print()
print()

mega = 0
tempoDeDownload = 0

arquivo = float(input("Qual tamanho do arquivo para download? MB  "))
velocidade = float(input("Qual a velocidade do link da Internet? Mbps"))

mega = velocidade * 8 
tempoDeDownload = arquivo / mega 

print('O tempo de Download do arquivo é de {} '.format(tempoDeDownload))

print("")
print("")

