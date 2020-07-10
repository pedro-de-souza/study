numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)

# 1
# 2
# 3

a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)

# 1
# 2
# [3, 4, 5, 6, 7, 8]
# 9

a, b, c, d, *e, f, g = range(20)
print(len(e))

# a=0
# b=1
# c=2
# d=3
# e=[4,5,6,7,8,9,10,11,12,13,14,15,16,17]
# f=18
# g=19

