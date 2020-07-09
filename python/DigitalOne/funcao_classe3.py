class Televisao:
    def __init__(self):
        self.ligada = False
    def  power(self):
        self.ligada = False if self.ligada else True

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
