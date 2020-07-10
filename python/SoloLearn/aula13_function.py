print("Hello world!")
range(2, 20)
str(12)
range(10, 20, 3)

# 

def my_func():
   print("spam")
   print("spam")
   print("spam")

my_func()

# 

def print_with_exclamation(word):
   print(word + "!")
    
print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")

# 

def print_sum_twice(x, y):
   print(x + y)
   print(x * y)

print_sum_twice(5, 8)

# 

def function(variable):
   variable += 1
   print(variable)

function(7)
print(variable)

# 

def max(x, y):
    if x >=y:
        return x
    else:
        return y
        
print(max(4, 7))
z = max(8, 5)
print(z)

# 

def shortest_string(x, y):
  if len(x) <= len(y):
      return x
  else:  
      return y

# 

def add_numbers(x, y):
  total = x + y
  return total
  print("This won't be printed")

print(add_numbers(4, 5))

# 

def multiply(x, y):
   return x * y

a = 4
b = 7
operation = multiply
print(operation(a, b))

# 

def add(x, y):
  return x + y

def do_twice(func, x, y):
  return func(func(x, y), func(x, y))

a = 5
b = 10

print(do_twice(add, a, b))

# 

def func(x):
  res = 0
  for i in range(x):
     res += i
  return res

print(func(4))