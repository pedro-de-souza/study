# Geralmente usado em declarações condicionais, all e any tomam uma lista como argumento e retornam True se todos ou algum (respectivamente) de seus argumentos forem avaliados como True (e False caso contrário).
# A função enumerar pode ser usada para iterar pelos valores e índices de uma lista simultaneamente.

nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
   print("Todos maiores que 5")

if any([i % 2 == 0 for i in nums]):
   print("Pelo menos um é par")

for v in enumerate(nums):
    print(v)
    # (0, 55)
    # (1, 44)
    # (2, 33)
    # (3, 22)
    # (4, 11)