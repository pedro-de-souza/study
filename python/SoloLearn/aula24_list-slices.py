#  List Slices/ Fatias de lista fornecem uma maneira mais avançada de recuperar valores de uma lista. O fatiamento básico de lista envolve a indexação de uma lista com dois números inteiros separados por dois pontos .

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6]) # [4, 9, 16, 25] 
print(squares[3:8] # [9, 16, 25, 36, 49] 
print(squares[0:1]) # [0]


# Se o primeiro número de uma fatia for omitido, será considerado o início da lista.
# Se o segundo número for omitido, será considerado o fim.

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])# [0, 1, 4, 9, 16, 25, 36]
print(squares[7:])#[49, 64, 81]

# 

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])#[0, 4, 16, 36, 64]
print(squares[2:8:3])#[4, 25]

# 1) primeiro parâmetro significa de onde começamos.
# 2) segundo parâmetro deve dizer onde parar. 
# 3) terceiro parâmetro a quantidade de número da lista.

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1]) #[1, 4, 9, 16, 25, 36, 49, 64]



