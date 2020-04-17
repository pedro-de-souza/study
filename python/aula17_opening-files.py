# Você pode usar o Python para ler e escrever o conteúdo dos arquivos .
# Arquivos de texto são os mais fáceis de manipular. Antes que um arquivo possa ser editado, ele deve ser aberto usando a função open.

myfile = open("arquivo.txt")


#Você pode especificar o modo usado para abrir um arquivo aplicando um segundo argumento à função abrir . Enviar "r" significa abrir no modo de leitura, que é o padrão. Enviar "w" significa modo de gravação, para reescrever o conteúdo de um arquivo. Enviar "a" significa modo de adição, para adicionar novo conteúdo ao final do arquivo. Adicionar "b" a um modo abre no modo binário , usado para arquivos que não são de texto (como arquivos de imagem e som)
# 

# write mode
open("arquivo.txt", "w")

# read mode
open("arquivo.txt", "r")
open("arquivo.txt")

# binary write mode
open("arquivo.txt", "wb") 

# Depois que um arquivo for aberto e usado, você deve fechá-lo. Isso é feito com o método close do objeto file.

file = open("filename.txt", "w")

file.close()