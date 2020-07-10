
# Os conjuntos de dados vêm de uma ampla variedade de fontes e formatos:
# podem ser coleções de medidas numéricas, corpus de texto, imagens, clipes de áudio ou basicamente qualquer coisa.
# Independentemente do formato, o primeiro passo na ciência de dados é transformá-lo em matrizes de números.

# Coletamos 45 alturas de presidente dos EUA em centímetros em ordem cronológica e as armazenamos em uma lista ,
# um tipo de dados embutido em python.
heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

cnt = 0
for height in heights:
  if height > 188:
    cnt +=1
print(cnt)