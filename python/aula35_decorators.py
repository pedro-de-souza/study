# Os decoradores fornecem uma maneira de modificar funções usando outras funções.
# Isso é ideal quando você precisa estender a funcionalidade das funções que não deseja modificar.
def decor(func):
  def wrap():
    print("============")
    func()
    print("============")
  return wrap

def print_text():
  print("Hello world!")

decorated = decor(print_text)
decorated()