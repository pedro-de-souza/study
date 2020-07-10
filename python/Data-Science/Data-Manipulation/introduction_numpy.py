# Numpy (abreviação de Nu amical Py thon) nos permite encontrar a resposta de
# quantos presidentes são mais altos que 188 cm com facilidade.
# Abaixo, mostramos como usar a biblioteca e comece com o objeto básico em numpy.

import numpy as np

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]
heights_arr = np.array(heights)
print((heights_arr > 188).sum())

# Uma classe de matriz em Numpy é chamada de matriz ndarray ou n-dimensional.
# Podemos usar isso para contar o número de presidentes em heights_arr, use o atributo numpy.ndarray.size :

print(heights_arr.size)

# Tamanho nos diz o tamanho da matriz, forma nos diz a dimensão. Para obter a forma atual de uma matriz, use a forma do atributo:
print(heights_arr.shape)