def function(named_arg, *args):
   print(named_arg)
   print(args)

function(1, 2, 3, 4, 5)

# 1
# (2, 3, 4, 5)

def AAon(x, y, food="spam"):
   print(food)

AAon(1, 2)
AAon(3, 4, "egg")

# spam
# egg 

def my_func(x, y=7, *args, **kwargs):
   print(kwargs)

my_func(2, 3, 4, 5, 6, a=7, b=8)

# {'a': 7, 'b': 8}