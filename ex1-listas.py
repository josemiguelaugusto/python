#Ler 5 numeros e guardar na lista
valores = []
maior = 0
menor = 2
for pos, num in enumerate(range(1,6)):
    valores.append(int(input(f"Digite o {num}º: ")))

#Mostar o maior e menor valor lidos e suas posições

for p, v in enumerate(valores):
    if valores[p] > maior:
        maior = valores[p]
    if valores[p] < menor:
        menor = valores[p]

print("#"*50)
print("Lista de valores= ", valores)
print(f"o Maior valor é= {maior}")
print(f"o Menor valor é= {menor}")
print("#"*50)