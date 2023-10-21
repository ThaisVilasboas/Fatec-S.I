

Salario= float(input("Digite o valor do salário do funcionário: "))

tempoEmpresa= int(input("Informe quanto tempo de empresa:" ))

if Salario <= 1000:
    if tempoEmpresa <= 3:
        Aumento = Salario*0.05 
        salarioFinal= Aumento+Salario
    else:
        Aumento = Salario*0.10 
        salarioFinal= Aumento+Salario
if Salario <= 3000:
    if tempoEmpresa <= 5:
        Aumento = Salario*0.15 
        salarioFinal= Aumento+Salario
    else:
        Aumento = Salario*0.20 
        salarioFinal= Aumento+Salario
else: 
    if tempoEmpresa <= 10:
        Aumento = Salario*0.25 
        salarioFinal= Aumento+Salario
    else:
        Aumento = Salario*0.30 
        salarioFinal= Aumento+Salario
        
print("Valor do aumento:",Aumento )
print("Valor do salário final: ", salarioFinal )
    
