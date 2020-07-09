
lista = [1,2]
try:
    divisao  = 10/1
    lista[1]
    # x = a
except ZeroDivisionError:
    print('Não é possível realizar essa divisão')
except IndexError:
    print('Posição não existe')
except BaseException as ex:
    print(ex)
# except:
#     print('Erro genérico')
else:
    print('Senão tiver exceção: Olha aqui.')
finally:
    print('Sempre executa')