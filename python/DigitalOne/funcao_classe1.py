class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def soma(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def multi(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b

calculadora = Calculadora(7,5)
print(calculadora.soma())
print(calculadora.sub())
print(calculadora.multi())
print(calculadora.div())

