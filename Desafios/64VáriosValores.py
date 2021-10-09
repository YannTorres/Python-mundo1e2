num = 0
c = 0
soma = 0
num = int(input('Digite um número (999 para parar): '))
while num != 999:
    c += 1
    soma = soma + num
    num = int(input('Digite um número (999 para parar): '))
print(f'Você digitou {c} termos e sua soma é {soma} ')
