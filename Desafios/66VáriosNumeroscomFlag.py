cont = soma = 0
while True:
    n1 = int(input('Digite um valor (999 para parar): '))
    if n1 == 999:
        break
    else:
        cont += 1
        soma += n1
print(f'Foram digitados {cont} números que somados dão {soma}')
