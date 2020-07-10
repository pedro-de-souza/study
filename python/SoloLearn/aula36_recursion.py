# A recursão é um conceito muito importante na programação funcional.
# A parte fundamental da recursão é a auto-referência - funções que se autodenominam. É usado para resolver problemas que podem ser divididos em subproblemas mais fáceis do mesmo tipo.

def factorial(x):
  if x == 1:
    return 1
  else: 
    return x * factorial(x-1)
    
print(factorial(4))