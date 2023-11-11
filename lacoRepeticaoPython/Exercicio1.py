#A) Maria vai ao supermercado e compra N produtos. Fazer
#um programa para ler o valor de cada um dos produtos e no
#final apresentar o total da conta que Maria tem que pagar.

quantidade = int(input("Quantos produtos são ?"))
valorTotal = 0
contador = 1
preco = 0 

while contador <= quantidade:
    preco = float(input(f"Preço do {contador}º produto: "))
    valorTotal = preco + valorTotal 
    contador = contador + 1
    
print("O valor total é :" , valorTotal )
