#14. Faça um programa que leia o sexo de 5 pessoas. No final calcule o número de pessoas do sexo masculino e o número de pessoas do sexo
#feminino.
 
contador  =   1
feminino  =   0
masculino =   0
XPessoas  =   5
 
while  contador <= 5:
    sexo = int(input("Informe o sexo da pessoa:\n => Feminino [1]\n => Masculino [2]\n "))
    
    if sexo == 1:
        feminino = feminino + 1
    
    elif sexo == 2:
        masculino =  masculino + 1
    
    TotalM = masculino
    TotalF = feminino
    contador = contador + 1
 
print("A Quantidade de pessoas do sexo masculino:",TotalM )
print("A Quantidade de pessoas do sexo feminino:",TotalF)
