#Suponha que Maria não sabe quantos produtos comprou.
#Então deve-se ir digitando os valores dos produtos e quando
#acabar digita-se o valor 0 para o produto. No final apresentar
#o total a ser pago.

  
valorTotal = 0
preco = 0 
parar = 1 
contador = 1


while parar == 1 :
    preco = float(input(f"Preço do {contador}º produto: "))
    valorTotal = preco + valorTotal 
    contador = contador + 1
    parar = int(input("Deseja acrescentar mais algum produto? \n ===> Sim (1) \n ===> Não (2) \n : " ))

print("O valor total é :%2.f" % valorTotal )
