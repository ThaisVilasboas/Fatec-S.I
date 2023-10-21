#8) Uma Empresa de fornecimento de INTERNET possui vários planos de assinatura. Para cada consumidor é digitado o tipo de
#plano e a quantidade MBytes consumido. O Valor do plano e o valor de cada MBytes consumido para cada tipo de consumidor é dado conforme a tabela
#abaixo:
#1 – Ouro, valor do plano=R$50,00, preço em reais por MB = R$ 0,30
#2 – Prata, valor do plano=R$30,00, preço em reais por MB = R$ 0,50
#3 – Bronze, valor do plano=R$20,00, preço em reais por MB = R$ 0,80
#Faça um programa que calcule o gasto final do assinante.


mb= float(input("Qual o valor de MB consumido: "))

plano= int(input("Tipo de plano que você possui:\n *Ouro(1) \n *Prata(2) \n *Bronze(3) \n "))
if plano ==1:
     ValorConsumo=  mb*0.30 + 50.00
elif plano ==2:
      ValorConsumo= mb*0.50 + 30.00 
elif plano ==3:
     ValorConsumo= mb*0.80 + 20.00 

print("Seu gasto final é de: ",ValorConsumo )

