distancia = float(input('Digite a distância da viagem: '))
if distancia > 200:
    print(f'Você deve pagar R$ {distancia * 0.45:.2f} por uma viagem de {distancia}KM')
else:
    print(f'Você deve pagar R$ {distancia * 0.50:.2f} por uma viagem de {distancia}KM')
