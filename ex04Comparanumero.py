#Ler dois valores inteiros e comparar:
#Quem é maior, menor ou serem iguais

#ler numeros
primeiroValor = int(input("Digite um numero inteiro: "))
segundoValor = int(input("Digite um numero inteiro: "))

if primeiroValor > segundoValor:
    print("O primeiro é maior")
elif segundoValor > primeiroValor:
    print("O Segundo é maior")
else:
    print("Não existe valor maior os dois são IGUAIS")
