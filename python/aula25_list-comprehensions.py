#List Comprehensions/compreensão de lista é uma maneira útil de criar rapidamente listas cujo conteúdo obedece a uma regra simples.

cubes = [i**3 for i in range(5)]

print(cubes)#[0, 1, 8, 27, 64]

nums = [i*2 for i in range(10)]

# Uma compreensão de lista também pode conter uma instrução if para impor uma condição aos valores da lista.

evens=[i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)# [0, 4, 16, 36, 64]