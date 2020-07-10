# É uma boa prática evitar desperdício de recursos, certificando-se de que os arquivos sejam sempre fechados após serem usados. Uma maneira de fazer isso é usar try e finalmente .

try:
   f = open("filename.txt")
   print(f.read())
finally:
   f.close()

# Uma forma alternativa de fazer isso é usando with declarações. Isso cria uma variável temporária (geralmente chamada f), que só é acessível no bloco recuado da instrução with .

with open("filename.txt") as f:
   print(f.read())