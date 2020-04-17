
# A formatação de string fornece uma maneira mais poderosa de incorporar não-strings dentro de strings. Formatação de strings usa uma seqüência de formato método para substituir uma série de argumentos na corda .

nums = [4, 5, 6]
msg ="Numbers:{0}{1}{2}". format(nums[0], nums[1], nums[2])
print(msg) #Numbers: 4 5 6

print("{0}{1}{0}".format("abra", "cad"))

a = "{x}, {y}".format(x=5, y=12)#5, 12

# O Python contém muitas funções e métodos internos úteis para realizar tarefas comuns.

# join - junta uma lista de strings com outra string como separador.
print(", ".join(["spam", "eggs", "ham"]))#prints "spam, eggs, ham"


# replace  - substitui uma substring em uma string por outra.
print("Hello ME".replace("ME", "world"))#prints "Hello world"


# startswith  e endswith - determina se há uma substring no início e no final de uma string , respectivamente.
print("This is a sentence.".startswith("This"))# prints "True"

print("This is a sentence.".endswith("sentence."))# prints "True"


# Para alterar o caso de uma sequência , você pode usar lower e upper .
print("This is a sentence.".upper())# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())#prints "an all caps sentence"


# A divisão do método é o oposto de join , transformando uma string com um determinado separador em uma lista.
print("spam, eggs, ham".split(", "))#prints "['spam', 'eggs', 'ham']"