# O filter de função filtra um iterável removendo itens que não correspondem a um predicado (uma função que retorna um booleano 

nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)