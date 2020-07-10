# As classes são criadas usando a palavra-chaveclasse e um bloco recuado, que contém métodos de classe (que são funções).

class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

# O __init__ método é o mais importante método em uma classe.
# Isso é chamado quando uma instância (objeto) da classe é criada, usando o nome da classe como uma função .

 
class Student:
  def __init__(self, name):
    self.name= name
test = Student("Bob")
print(test.name)
 
#  As classes podem ter outros métodos definidos para adicionar funcionalidade a elas.
# Lembre-se de que todos os métodos devem ter self como seu primeiro parâmetro .


class Dog:
    legs = 4
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Woof!")

fido = Dog("Fido", "brown")
print(fido.name)
print(fido.legs)
fido.bark()
