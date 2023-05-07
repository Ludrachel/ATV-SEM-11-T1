dep_inicial = float(input())
taxa_juros = float(input())
cont = dep_inicial
anos = 0
while cont < (dep_inicial * 2):
    cont += cont * (taxa_juros/100)
    anos += 1
print(anos)
