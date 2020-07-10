import numpy as np

heights_arr = np.array([189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191])
ages_arr = np.array([57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]).reshape((-1,1))

heights_arr = heights_arr.reshape((45,1))
height_age_arr = np.hstack((heights_arr, ages_arr))


print(height_age_arr[:,0]*0.0328084)
# Executar operações matemáticas em matrizes é simples. Por exemplo, para converter as alturas de centímetros em pés,
# sabendo que 1 centímetro é igual a 0,0328084 pés, podemos usar a multiplicação:

# Agora temos todas as alturas em pés. Observe que essa operação não altera a matriz original, ela retorna um novo 1darray
# em que 0,0328084 foi multiplicado para cada elemento na primeira coluna de 'heights_age_arr'.

# Além disso, existem vários métodos em numpy para executar cálculos mais complexos em matrizes. Por exemplo, o método sum () encontra a soma de todos os elementos em uma matriz:
print(height_age_arr.sum())
print(height_age_arr.sum(axis=0))
# Outras operações, como .min (), .max (), .mean (), funcionam de maneira semelhante a .sum ().

# Comparações
print('Comparações')
# Na prática da ciência de dados, geralmente encontramos comparações para identificar
# linhas que correspondem a determinados valores. Podemos usar operações
# incluindo "<", ">", "> =", "<=" e "==" para fazer isso.
# Por exemplo, no conjunto de dados height_age_arr, podemos estar interessados ​​apenas nos presidentes que
# iniciaram sua presidência com menos de 55 anos.

print(height_age_arr [:, 1] <55)

# Mask & Subsetting

# Agora que as linhas correspondentes a certos critérios podem ser identificadas,
# um subconjunto dos dados pode ser encontrado.
# Por exemplo, em vez de todo o conjunto de dados, queremos apenas presidentes altos,
#  ou seja, presidentes cuja altura seja maior ou igual a 182 cm

print('Mask & Subsetting')
mask = height_age_arr[:, 0] >= 182
print(mask.sum())

tall_presidents = height_age_arr[mask, ]
tall_presidents.shape

print(tall_presidents.shape)

# Vários critérios
# Podemos criar uma máscara que atenda a mais de um critério. Por exemplo, além da estatura, queremos encontrar os presidentes com 50 anos ou menos no início de sua presidência.
# Para conseguir isso, usamos & para separar as condições e cada condição é encapsulada com parênteses "()", como mostrado abaixo:

print('Vários critérios')
mask_criteria = (height_age_arr[:, 0]>=182) & (height_age_arr[:,1]<=50)

print(height_age_arr[mask_criteria,])