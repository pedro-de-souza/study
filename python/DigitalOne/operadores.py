# a = 10
# b = 5
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
soma = a+b
sub = a - b
mult = a * b
div = a /b
rest = a % b

# print(type(soma))

print('\n Soma: '+str(soma))
print(' Subtração: '+str(sub))
print(' Mutiplicação: '+str(mult))
print(f' Divisão: {div:.0f}')
# print(' Divisão: {:.0f}'.format(div))
print(' Resto da divisão: {resto}'.format(resto=rest))