class Animal: 
  def __init__(self, name, color):
    self.name = name
    self.color = color

class Cat(Animal):
  def purr(self):
    print("Purr...")
        
class Dog(Animal):
  def bark(self):
    print("Woof!")

fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()

class A:
  def spam(self):
    print(1)

class B(A):
  def spam(self):
    print(2)
    super().spam()
            
B().spam()