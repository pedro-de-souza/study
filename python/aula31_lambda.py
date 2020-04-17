# Uma função lambda é uma pequena função anônima.
# Uma função lambda pode receber qualquer número de argumentos, mas pode ter apenas uma expressão.

def my_func(f, arg):
  return f(arg)

my_func(lambda x: 2*x*x, 5)


#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambda
print((lambda x: x**2 + 5*x + 4) (-4))

# 

double = lambda x: x * 2 
print (double (7))

#  

triple = lambda x: x * 3
add = lambda x, y: x + y
print(add(triple(3), 4))


# 

nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
nums = filter(lambda x: x > 1, nums)
print(len(list(nums)))