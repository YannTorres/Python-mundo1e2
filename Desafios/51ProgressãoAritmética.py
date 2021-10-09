print('=' * 20)
print('10 Termos de uma PA')
print('=' * 20)
a = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
for c in range(a, a + (10 * r), r):
    print(c, end=' -> ')
print('FIM')