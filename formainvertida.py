num = int(input())
num_reverso = 0
while num != 0:
    digito = num % 10
    num_reverso = (num_reverso * 10) + digito
    num = num // 10
print(num_reverso)
