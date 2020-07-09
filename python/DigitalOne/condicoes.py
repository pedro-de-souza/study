a = int(input(' Digite a primeira nota: '))
b = int(input(' Digite a degunda nota: '))
c = int(input(' Digite a terceira nota: '))
d = int(input(' Digite a quarta nota: '))

if a < 0 or a > 10 or b < 0 or b > 10 or c < 0 or c > 10 or d < 0 or d > 10:
    print(' Digite nomeros entre 0 a 10')
else:
    media = (a+b+c+d)/4
    if media > 8:
        print(f' Sua média final é {media:.1f}: Congratulations')
    elif media > 5:
        print(f' Sua média final é {media:.1f}: Parabéns.')
    else:
        print(f' Sua média final é {media:.1f}: Não foi dessa vez.')



# a = int(input(' Digite um número: '))
# b = int(input(' Digite outro número: '))
#
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or resto_b == 0:
#     print(' número par')
# elif resto_a == 0 or not resto_b == 0:
#     print(' número impar')





# a = int(input(' Primeiro valor: '))
# b = int(input(' Segundo valor: '))
# c = int(input(' Terceiro valor: '))
#
# if a > b and a > c:
#     print(' o número {a} é maior que {b} e {c}'.format(a=a,b=b, c=c))
# elif b < a and b >c :
#     print(' o número {b} é maior que {a} e {c}'.format(a=a, b=b, c=c))
# else:
#     print(' o número {c} é maior que {a} e {b}'.format(a=a, b=b, c=c))