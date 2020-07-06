# Os métodos dos objetos que examinamos até agora são chamados por uma instância de uma classe, que é então passada para o parâmetro auto do método . 
# Os métodos de classe são diferentes - eles são chamados por uma classe, que é passada para o parâmetro cls do método .

class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def calculate_area(self):
    return self.width * self.height

  @classmethod
  def new_square(cls, side_length):
    return cls(side_length, side_length)

square = Rectangle.new_square(5)
print(square.calculate_area())

# 25

# Métodos estáticos são semelhantes aos métodos de classe, exceto que eles não recebem argumentos adicionais

class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings

  @staticmethod
  def validate_topping(topping):
    if topping == "pineapple":
      raise ValueError("No pineapples!")
    else:
      return True

ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
  pizza = Pizza(ingredients) 