cont = 0
soma = 0
while True:
    num = int(input())
    if cont != 0:
        media = soma / cont
    if num == 0:
        break
    soma += num
    cont += 1
if cont != 0:
    print(f'{media:.2f}')
