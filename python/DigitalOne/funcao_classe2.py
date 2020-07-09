class Calculadora:
    # def __init__(self):
    #     pass
    def soma(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
    def multi(self, a, b):
        return a * b
    def div(self, a, b):
        return a / b

calculadora = Calculadora()
print(calculadora.soma(7,5))
print(calculadora.sub(7,5))
print(calculadora.multi(7,5))
print(calculadora.div(7,5))

