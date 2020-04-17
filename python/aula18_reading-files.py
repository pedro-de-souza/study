# O conteúdo de um arquivo que foi aberto no modo de texto pode ser lido usando o método read .
file = open("arquivo.txt", "r")
cont = file.read()
print(cont)
file.close()

# Para ler apenas uma certa quantidade de um arquivo, você pode fornecer um número como argumento para a função de leitura . Isso determina o número de bytes que devem ser lidos. Você pode fazer mais chamadas para ler no mesmo objeto de arquivo para ler mais do arquivo byte a byte. Sem argumento , read retorna o restante do arquivo.

file = open("arquivo.txt", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()

# Após a leitura de todo o conteúdo de um arquivo, qualquer tentativa de leitura posterior desse arquivo retornará uma sequência vazia , porque você está tentando ler a partir do final do arquivo.

file = open ("filename.txt", "r") 
file.read() 
print ("releitura") 
print (file.read ()) 
print ("Finished") 
file.close()

# Para recuperar cada linha em um arquivo, você pode usar o método readlines para retornar uma lista na qual cada elemento é uma linha no arquivo.

file = open("filename.txt", "r")
print(file.readlines())
file.close()
# ['Line 1 text \n', 'Line 2 text \n', 'Line 3 text']
file = open("filename.txt", "r")

for line in file:
    print(line)

file.close() 
# Line 1 text...

