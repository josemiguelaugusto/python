#Saber o valor do imovel
from time import process_time_ns

precoImovel = float(input("Qual o valor do imovel que pretende comprar?: "))
#Salario do comprador
salarioComprador = float(input("Quanto é a renda salarial?: "))
#Saber em quanto tempo ele vai pagar a casa
tempoDePagamento = int(input("Em quantos anos pretende concluir o pagamento do imovel?: "))
#Saber o preço das prestações mensais/ esse preço não pode exceder 30% do seu salario senão sera negado o emprestimo
aprovaEmprestimo = False
pretacaoMensal = (precoImovel /(tempoDePagamento*12))
if(pretacaoMensal < (0.3*salarioComprador)):
    aprovaEmprestimo = "Aprovado"
else:
    aprovaEmprestimo = "Negado"

print(f"Preço: {precoImovel}, Salário: {salarioComprador}, Tempo: {tempoDePagamento}, Prestação Mensal: {pretacaoMensal:.2f}€"
      f"\nSituação Do Emprestimo: {aprovaEmprestimo} ")