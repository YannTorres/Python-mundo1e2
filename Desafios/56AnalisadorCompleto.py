conti = 0
maisvelho = 0
nomemaisvelho = ''
conts = 0
for c in range(1, 5):
    print(f'------{c}ªPessoa------')
    nome = str(input('Nome: ').capitalize().strip())
    idade = float(input('Idade: '))
    sexo = input('Sexo [M / F]: ').strip()
    conti = conti + idade
    if c == 1 and sexo in 'Mm':
        maisvelho = idade
        nomemaisvelho = nome
    elif sexo in 'Mm' and idade > maisvelho:
        maisvelho = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade >= 20:
        conts = conts + 1
print(f'A média de idades é {conti/4:.1f}')
print(f'O Homem mais velho tem {maisvelho:.0f} anos e se chama {nomemaisvelho}')
print(f'Existe {conts} mulher(es) com idade maior que 20 anos')
