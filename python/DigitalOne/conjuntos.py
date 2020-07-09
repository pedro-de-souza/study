conjunto = {1,2,3,4}
conjunto1 = {1,2,3,4}
conjunto2 = {5,6,7,8}
conjuntos1e2 = conjunto1.union(conjunto2)

print(conjuntos1e2)

conjunto_intersection = conjunto1.intersection(conjunto)
conjunto_diferenca = conjunto.difference(conjunto2)
conjunto_simetrico = conjunto.symmetric_difference(conjunto2)

print(conjunto)
print(conjunto_intersection)
print(conjunto_diferenca)
print(conjunto_simetrico)


print(conjunto)
conjunto.add(5)
conjunto.discard(1)

print(conjunto1)
print(conjunto2)
print(conjuntos1e2)

conjunto_a = {1,2,}
conjunto_b = {1,2,3,4}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print(conjunto_subset)
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print(conjunto_superset)

lista = ['cachorro', 'gato', 'gato', 'elefante']
conjunto_animais = set(lista)
lista = list(conjunto_animais)
print(conjunto_animais)