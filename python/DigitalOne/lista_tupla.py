lista = [1,3,5,4,2]
lista_animal = ['cachorro','gato','elefante']
nova_lista = lista*3
tupla = (1,10,15,5)
tupla_animal = tuple(lista_animal)

print(tupla)
print(len(tupla))
print(tupla_animal)

lista_num = list(tupla)
print(type(lista_num))

for i in lista_animal:
    print(i)

lista.sort()
lista_animal.reverse()

print(lista)
print(sum(lista))
print(max(lista))
print(nova_lista)


if 'lobo' in lista_animal:
    print('lobo')
else:
    print('Adicionando lobo na lista')
    lista_animal.append('lobo')

print(lista_animal)
lista_animal.pop(1)
lista_animal.remove('elefante')
print(lista_animal)