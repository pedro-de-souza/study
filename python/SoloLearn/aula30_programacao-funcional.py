# A programação funcional é um estilo de programação que (como o nome sugere) se baseia em funções.
# Uma parte essencial da programação funcional são as funções de ordem superior . Vimos essa ideia brevemente na lição anterior sobre funções como objetos. Funções de ordem superior assumem outras funções como argumentos ou as retornam como resultados.

def apply_twice(func, arg):
   return func(func(arg))

def add_five(x):
   return x + 5

print(apply_twice(add_five, 10))#20

# 

def test(func, arg):
  return func(func(arg))

def mult(x):
  return x * x

print(test(mult, 2))#16

# A programação funcional procura usar funções puras . As funções puras não têm efeitos colaterais e retornam um valor que depende apenas de seus argumentos.
# É assim que as funções da matemática funcionam: por exemplo, O cos (x), pelo mesmo valor de x, sempre retornará o mesmo resultado.


# Funções puras
# Uma função pura é muito mais fácil de entender, especialmente porque nossa base de código pode escalar, além de funções baseadas em funções que executam um trabalho e o fazem bem. As funções puras não modificam variáveis ​​/ estado / dados externos fora do escopo e retornam a mesma saída, com a mesma entrada. Portanto, é considerado "puro".
def pure_function(x, y):
  temp = x + 2*y
  return temp / (2*x + y)


# Funções impuras
# Uma função impura é uma função que modifica variáveis ​​/ estado / dados fora de seu escopo lexical, considerando-a "impura" por esse motivo. Termos de funções impuras / puras, podemos escrever um código que é muito mais fácil de raciocinar.
some_list = []

def impure(arg):
  some_list.append(arg)