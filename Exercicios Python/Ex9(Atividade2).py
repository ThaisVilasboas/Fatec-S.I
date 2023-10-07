#9)Faça um algoritimo/programa que leia o sálario bruto de um funcionário e calcule
#o salário liquido sabendo que são cobrados 11% de inss(limitado a valor máximo de R$820.00)
#e o imposto de renda é cobrado conforme a tabela abaixo:
#salarioLiquido=salariobruto-inss-ir
#salario: (<1500 = 10%IR), (>=1500 = 20%IR)



salarioBruto = float(input("Digite o valor do salário: "))
inss = salarioBruto * 0.11
if(inss > 820.00 ):
    inss = 820.00

if(salarioBruto <1500):
    ir = salarioBruto * 0.10 
if(salarioBruto >=1500):
    ir = salarioBruto * 0.20 
    
salarioLiquido = salarioBruto - inss - ir
print("O salário com os descontos ficará: ", salarioLiquido)
