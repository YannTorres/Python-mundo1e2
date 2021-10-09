nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1+nota2) / 2
print(f'A média do aluno foi {media:.2f}')
if media < 5:
    print('O aluno está reprovado')
elif media >= 7:
    print('O aluno está aprovado')
else:
    print('O aluno está de recuperação')
