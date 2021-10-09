import datetime
ano = int(input('Ano de nascimento: '))
idade = datetime.date.today().year - ano
tempo = 18 - idade
tempo2 = idade - 18
print(f'Quem nasceu em {ano} tem {idade} anos em {datetime.date.today().year}')
if idade < 18:
    print(f'Ainda falta {tempo} ano(s) para o alistamento')
    print(f'Seu alistamneto será em {datetime.date.today().year + tempo}')
elif idade > 18:
    print(f'Você deveria ter se alistado em {tempo2} ano(s)')
    print(f'Seu alistamento deveria ter acontecido em {datetime.date.today().year - tempo2}')
else:
    print(f'Você deve se alistar IMEDIATAMENTE')
