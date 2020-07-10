
# O módulo itertools é uma biblioteca padrão que contém várias funções que são úteis na programação funcional.

from itertools import accumulate, takewhile,count,product

for i in count(3):
  print(i)
  if i >=11:
    break

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x<= 6, nums)))

a={1, 2}
print(len(list(product(range(3), a))))

