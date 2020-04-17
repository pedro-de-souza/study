# Este é um projeto de exemplo, mostrando um programa que analisa um arquivo de amostra para descobrir qual porcentagem do texto cada caractere ocupa.
# Esta seção mostra como um arquivo pode ser aberto e lido.

filename = input("Enter a filename: ")

with open(filename) as f:
   text = f.read()

print(text)

# Esta parte do programa mostra uma função que conta quantas vezes um caractere ocorre em uma string.

def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count

# Essa função usa como argumentos o texto do arquivo e um caractere, retornando o número de vezes que esse caractere aparece no texto.
filename = input("Enter a filename: ")
with open(filename) as f:
  text = f.read()

print(count_char(text, "r"))

# A próxima parte do programa encontra qual porcentagem do texto cada caractere do alfabeto ocupa.

def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count

filename = input("Enter a filename: ")
with open(filename) as f:
  text = f.read()

for char in "abcdefghijklmnopqrstuvwxyz":
  perc = 100 * count_char(text, char) / len(text)
  print("{0} - {1}%".format(char, round(perc, 2)))


# Ele é usado para garantir finalização de recursos adquiridos.

# Um arquivo, por exemplo é aberto. Quem garante que ele será fechado? Mesmo que você coloque no código de forma explícita que ele deve ser fechado, se ocorrer uma exceção, o código sai de escopo sem executar o resto do código que está em escopo, ele pula o fechamento.

# Para evitar isto usamos um try finally. O finally garante a finalização. Como o código fica um pouco longo e este caso é bastante frequente a linguagem providenciou uma forma simplificada com o with.