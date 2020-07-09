
while True:
    print('\n Simulador de 4 notas:')
    a = int(input(' Digite a primeira nota: '))
    b = int(input(' Digite a degunda nota: '))
    c = int(input(' Digite a terceira nota: '))
    d = int(input(' Digite a quarta nota: '))

    if (0 > a < 10) or (0 > b < 10) or (0 > c < 10) or (0 > d < 10):
        print(' Digite nomeros entre 0 a 10')
    else:
        break

media = (a+b+c+d)/4
if media > 8:
    print(f' Sua média final é {media:.1f}: Congratulations')
elif media > 5:
    print(f' Sua média final é {media:.1f}: Parabéns.')
else:
    print(f' Sua média final é {media:.1f}: Não foi dessa vez.')