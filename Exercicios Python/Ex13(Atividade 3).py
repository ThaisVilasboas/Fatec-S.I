#13) Faça um programa que calcule o novo salário do funcionário:



salario= float(input("Digite o valor do Salário do funcionário:"))

if salario<= 1000:
    salarioAtual= salario*0.15+salario
elif salario > 1000:
    salarioAtual= salario*0.10+salario
elif salario > 2000:
    salarioAtual= salario*0.05+salario
elif salario > 3000:
    salarioAtual= salario*0.03+salario
    
print ("O valor do salário atual é", salarioAtual)     
