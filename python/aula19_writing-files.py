# Para gravar em arquivos, use o método write , que grava uma string no arquivo
file = arquivo open("newfile.txt", "w") 
file.write("Isso foi gravado em um arquivo") 
file.close() 

file = open("newfile.txt", "r") 
print (file.read()) 
file.close()

# Quando um arquivo é aberto no modo de gravação, o conteúdo existente do arquivo é excluído.
file = open("newfile.txt", "r") 
print("Lendo o conteúdo inicial") 
print(file.read()) 
print("Finalizado") 
file.close() 

file = open("newfile.txt" , "w") 
file.write("Algum novo texto") 
file.close() 

file = open("newfile.txt", "r") 
print("Lendo novos conteúdos") 
print(file.read ()) 
print("Finalizado") 
file.close ()

# O método write retorna o número de bytes gravados em um arquivo, se for bem-sucedido.

msg = "Hello world!"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written) #12
file.close()