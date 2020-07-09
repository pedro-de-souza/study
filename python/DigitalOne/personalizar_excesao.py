class Error(Exception):
    pass
class InputError(Error):
    def __init__(self, message):
        self.message = message


while True:
    try:
        x = int(input('Digite uma nota de 0 a 10: '))
        if x<0 or x > 10:
            raise InputError('Digite somente uma nota entre 0 a 10')
        else:
            print(x)
        break
    except ValueError:
        print('Valor inválido. Digite apenas números')
    except InputError as ex:
        print(ex)