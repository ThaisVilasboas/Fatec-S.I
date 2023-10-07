#2) Faça um algoritmo/programa que leia o valor de um
#produto e se o produto for nacional cobrar 5% de imposto,
#se for importado cobrar 10% de imposto. Calcular o valor
#final do produto.


print("Calculo do valor de imposto:")
valorDoProduto=float(input("Digite o valor do produto:"))
produtoNacional=int(input("Produto Nacional(Digite 1):\n Produto internacional(Digite 2): "))
if(produtoNacional == 1):
    ValorDoProduto=valorDoProduto*0.05
