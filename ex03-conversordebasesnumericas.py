#Menu escolha de conversão

def Conversor(numero):
    #numero = int(input("Digite um numero inteiro: "))
    print("""
    1-Binario
    2-Octal
    3-Hexadecimal
    """)
    escolha = str(input("Escolha a base de conversão: "))

    match escolha:
        case "1":
            return bin(numero)
        case "2":
            return oct(numero)
        case "3":
           return hex(numero)
        case _:
            print("Escolha Invalida!!!")
numero = int(input("Digite um numero inteiro: "))
print(Conversor(numero))