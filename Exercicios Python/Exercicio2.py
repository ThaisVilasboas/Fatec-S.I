#2) Calcular o valor da conta de Energia de uma residência
#sabendo-se que o valor do Kw é de R$0,30.
#Mas como estamos em um período de seca então utiliza-se
#BANDEIRA VERMELHA, o que proporciona um acréscimo de
#10% no valor da conta.
#Faça um pseudocódigo/algoritmo que calcule o valor da conta


precoKw=0.30
consumoKw=int(input("Digite a quantidade Kw comsumida: "))
valorDaConta=consumoKw*precoKw
acrescimo=valorDaConta*10/100
valorDaConta=valorDaConta+acrescimo
print("Valor total da conta com acréscimo de 10%: ", valorDaConta)

