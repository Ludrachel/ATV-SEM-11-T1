num_maior = 0
num_menor = 99999999
while True:
    num = int(input())
    if num == 0:
        break
    if num > num_maior:
        num_maior = num
    if num < num_menor:
        num_menor = num
if num_maior != 0 and num_menor != 99999999:
    print(num_maior)
    print(num_menor)
    

