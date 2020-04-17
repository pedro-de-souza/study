# O mapa e o filtro de funções integradas são funções de ordem superior muito úteis que operam em listas (ou objetos semelhantes chamados iteráveis ).

def add_five (x): 
  return x + 5 

nums = [11, 22, 33, 44, 55] 
result = list ( map (add_five, nums)) 
print (result)