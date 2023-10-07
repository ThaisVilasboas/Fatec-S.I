#6) faça um programa que recebe a idade de um nadador
#e classifique-o numa das seguintes categorias:


idade = float(input("Digite a idade do nadador:" ))
if idade >= 18:
   print ("Adulto")
elif idade >=14 and idade <18:
   print ("Juvenil")
elif idade >=9 and idade <14:
    print("infantil")
else:
    print("Mirim")
