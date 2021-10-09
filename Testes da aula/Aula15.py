s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    else:
        s = s + n
print(f'a soma vale {s}')
