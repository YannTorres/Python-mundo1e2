texto = str(input('Digite seu nome completo: ')).strip()
texto1 = texto.split()
texto2 = ''.join(texto1)

print(f'Seu nome somente em maiúsculas fica: {texto.upper()}')
print(f'Seu nome somente em minúsculas fica: {texto.lower()}')
print(f'Seu primeiro nome tem: {len(texto1[0])} letras')
print(f'Seu nome tem: {len(texto2.strip())} letras')
