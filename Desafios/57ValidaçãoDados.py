sexo = 1
while sexo != 'm' and sexo != 'f':
    sexo = input('Informe o seu sexo [M/F]: ').lower().strip()[0]
    if sexo != 'm' and sexo != 'f':
        print('Opção invalida tente novamente!')
    elif sexo == 'm' or sexo == 'f':
        if sexo == 'm':
            print('Sexo Masculino resgistrado com sucesso!')
        else:
            print('Sexo Feminino resgistrado com sucesso!')
