salario = float(input())
divida = float(input())
mes = 10
ano = 2016
while divida < salario:
    mes += 1
    divida += divida * 0.15
    if mes > 12:
        mes = 1
        ano += 1
    if mes == 3:
        salario += salario * 0.05
        
print(f'{mes}/{ano}')
