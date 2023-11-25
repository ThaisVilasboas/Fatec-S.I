
quantPessoas = int(input("Digite a quantidade de pessoas:"))
contador = 1 
magro = 0
normal = 0
gordo = 0

while contador <= quantPessoas:
    peso = float(input(f"Digite o peso da {contador}º pessoa:"))
    altura = float(input(f"Digite a altura da {contador}º pessoa: "))
    imc = peso / altura*altura
    
    if imc < 18.5 :
        magro =  magro + 1

    elif imc <= 25 :
        normal =  normal + 1   
    
    else:
        gordo = gordo + 1
    
    contador = contador + 1
    
print("A Quantidade de pessoas magras é: ", magro )
print("A Qauntidade de pessoas normais é: ", normal )
print("A Qauntidade de pessoas gordas é: ", gordo )
