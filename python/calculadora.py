while True: 
    print("Options:")
    print("Digite '+' para adicionar dois números") 
    print("Digite '-' para subtrair dois números") 
    print("Digite '*' para multiplicar dois números") 
    print("Digite '/' para dividir dois números") 
    print("Digite '!' para finalizar o programa") 
    user_input = input(":")
    print(user_input) 

    if user_input == "!":
        break
    elif  user_input == "+": 
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: ")) 
        print("Resultado"+ num1+num2)

    elif  user_input == "-": 
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: ")) 
        print("Resultado"+ num1-num2)
   
    elif  user_input == "*": 
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: ")) 
        print("Resultado"+ num1*num2)
      
    elif  user_input == "/": 
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: ")) 
        print("Resultado"+ num1//num2)
       
    else:
        print("Digita algum numero valido")