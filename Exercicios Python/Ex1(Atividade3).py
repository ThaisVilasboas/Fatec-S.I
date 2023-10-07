#1) Elabore um programa que some 2 NOTAS digitadas pelo usuário.
#Calcule a média aritmética destas notas e apresente a seguinte
#mensagem:

notaA = float(input("Digite o valor da sua nota 1:" ))
notaB = float(input("Digite o valor da sua nota 2:" ))

media = (notaA + notaB) / 2
if media <4:
    print("Reprovado")
elif media <6:
    print("Exame") 
else: 
    print("Aprovado")
