
# Conjuntos são estruturas de dados, semelhantes a listas ou dicionários. Eles são criados usando chaves, ou a função set . Eles compartilham alguma funcionalidade com listas

num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])

print(3 in num_set)
print("spam" in word_set)


nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)

nums = {"a", "b", "c", "d"}
 
nums.add("z")
print(len(nums))

# Os conjuntos podem ser combinados usando operações matemáticas.
# O operador sindical | combina dois conjuntos para formar um novo contendo itens em ambos.
# O operador de interseção e obtém itens apenas em ambos.
# O operador de diferença - obtém itens no primeiro conjunto, mas não no segundo.
# O operador de diferença simétrica ^ obtém itens em um dos conjuntos, mas não em ambos.

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)