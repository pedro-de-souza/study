# A maioria dos códigos Python é um módulo a ser importado ou um script que faz alguma coisa.
# No entanto, às vezes é útil criar um arquivo que possa ser importado como um módulo e executado como um script.
# Para fazer isso, insira o código do script se __name__ == "__main__" .
# Isso garante que não será executado se o arquivo for importado.

def function():
   print("This is a module function")

if __name__=="__main__":
   print("This is a script")

# This is a script

