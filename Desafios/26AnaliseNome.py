n = str(input('Digite uma frase: ')).strip().lower()

print(f'A letra A aparece {n.count("a")} vezes na frase')
print(f'A primeira letra A aparece {n.find("a")+1}')
print(f'A primeira letra A aparece {n.rfind("a")+1}')

