# Geradores são um tipo de iterável , como listas ou tuplas.
# Ao contrário das listas, eles não permitem a indexação com índices arbitrários, mas ainda podem ser iterados com loops for .

def countdown():
    i=5
    while i > 0:
        yield i
        i -= 1

for i in countdown():
    print(i)

# def y():
#     yield 10
# i = y()
# next(i)

def numbers(x):
  for i in range(x):
    if i % 2 == 0:
      yield i

print(list(numbers(11)))


def make_word():
  word = ""
  for ch in "spam":
    word +=ch
    yield word

print(list(make_word()))

def power(x, y):
  if y == 0:
    return 1
  else:
    return x * power(x, y-1)
		
print(power(2, 3))