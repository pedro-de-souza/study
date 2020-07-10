import numpy as np

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

heights_and_ages = heights + ages
# converter uma lista em uma matriz numpy
heights_and_ages_arr = np.array(heights_and_ages)
print(heights_and_ages_arr.shape)

# Isso produz uma matriz longa. Seria mais claro se pudéssemos alinhar altura e idade para cada presidente e
# reorganizar os dados em uma matriz de 2 por 45, onde a primeira linha contém todas as alturas e a segunda linha contém idades.
# Para conseguir isso, uma nova matriz pode ser criada chamando numpy.ndarray.reshape com novas dimensões especificadas em uma tupla:
print(heights_and_ages_arr.reshape((2,45)))


arr1 = np.array([1,2,3,4,5,6])
print(arr1.shape)
# >> (6,) #before e after remodelar o número de elementos na matriz e os elementos será o mesmo.
arr2 = arr1.reshape(3,2)
print(arr2)# >> [[1, 2], [3, 4], [5, 6]]
print(arr2.shape) # >> (3, 2) #we pode remodelar com (3,2) a forma aqui, como 3 e 2 são múltiplos de 6
# arr3 = arr1.reshape (5,1) # Leva a erro (ValueError: não é possível remodelar a matriz do tamanho 6 na forma (5,1) )

# Outra característica do array numpy é que ele é homogêneo , o que significa que cada elemento deve ser do mesmo tipo de dados.
#
# Por exemplo, em heights_arr, registramos todas as alturas em números inteiros;
# portanto, cada elemento é armazenado como um número inteiro na matriz.
# Para verificar o tipo de dados, use numpy.ndarray.dtype

print(heights_and_ages_arr.dtype)