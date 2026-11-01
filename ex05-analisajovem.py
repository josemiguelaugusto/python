#Programa que vai analisar idades dos jovens para saber se ainda se podem alistar para o exercito
#Deve ter 18 para se alistar
#Ler ano de nascimento e saber a idade
import  datetime
nascimento = int(input("Em que ano voce nasceu: "))
idade = (datetime.date.today().year) - nascimento
#Ainda vai poder se alistar e quanto tempo falta
if idade < 18:
    print(f"Falta {18-idade} ano/s para se alistar")
elif idade > 18:
    print(f"Ja passou da hora, {idade-18} ano/s fora do prazo")
elif idade == 18:
    print(f"Esta na hora de se alistar, Vai Soldado!!")
else:
    print("Caso Desconhecido")