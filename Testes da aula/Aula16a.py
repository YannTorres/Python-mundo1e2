lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1])
print(lanche[1:])
print(lanche[-3:])
print(len(lanche))
for c in range(0, len(lanche)):
    print(lanche[c])
print('-' * 10)
for c in lanche:
    print(c)
print('-' * 10)
for pos, comida in enumerate(lanche):
    print(f'Eu comi {comida} na posição {pos}')
print('-' * 10)
for c in range(0, len(lanche)):
    print(f'Eu comi {lanche[c]} na posição {c}')
