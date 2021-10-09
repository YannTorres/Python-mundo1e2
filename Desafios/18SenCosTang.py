from math import sin,cos,tan, radians
angulo = float(input('Digite o valor do ângulo: '))
rad = radians(angulo)

sen = sin(rad)
cosa = cos(rad)
tang = tan(rad)

print(f'O COSSENO é {cosa:.2f}\nO SENO é {sen:.2f}\nA TANGENTE é {tang:.2f}')
