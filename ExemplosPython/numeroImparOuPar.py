#Dados um valor N, faça um programa que verifica se esse
#número é divisível por 2(então o número N é par, senão é impar)
#ou se é divisível por 5, ou se é divisível por ambos.
#DICA: utilizar o operador de módulo %
#Resto= 5%2 ➔ resto =1
#Resto= 10%2 ➔ resto =0



numero=int(input("Digite um número: "))
if numero%2 ==0:
    print("O número digitado é par. ")
else: 
    print("O número digitado é impar. ")
