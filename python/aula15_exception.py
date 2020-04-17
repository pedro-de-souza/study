# Exceção é um evento que ocorre devido a código ou entrada incorreta
# Manipulação de exceção
try:
   num1 = 7
   num2 = 0
   print (num1 / num2)
   print("Cálculo concluído")
except ZeroDivisionError:
   print("Ocorreu um erro")
   print("devido à divisão zero")

#   

try:
   variable = 10
   print(variable + "hello")
   print(variable / 2)
except ZeroDivisionError:
   print("Divided by zero")
except (ValueError, TypeError):
   print("Error occurred")

# Uma instrução de exceção sem nenhuma exceção especificada capturará todos os erros. Eles devem ser usados ​​com moderação, pois podem detectar erros inesperados e ocultar erros de programação.
# 
# 
# Para garantir que algum código seja executado, independentemente de quais erros ocorram, você pode usar uma instrução finally . A instrução finally é colocada na parte inferior de uma instrução try / except . O código em uma instrução finally sempre é executado após a execução do código nos blocos try e, possivelmente, nos blocos exceto .
# 

try:
   print("Hello")
   print(1 / 0)
except ZeroDivisionError:
   print("Dividido por zero")
finally:
   print("Este código será executado independentemente do que") 

#  Você pode gerar exceções usando a instrução raise. Você precisa especificar o tipo de exceção gerada.

print(1)
raise ValueError
print(2)

#  Nos blocos exceto , a instrução raise pode ser usada sem argumentos para aumentar novamente qualquer exceção ocorrida.
try:
   num = 5 / 0
except:
   print("An error occurred")
   raise
