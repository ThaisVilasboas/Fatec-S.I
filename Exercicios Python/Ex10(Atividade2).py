#10. Calcular as raízes da equação de 2 grau:


import math

A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))

Delta=A*B - 4*A*C
print("Delta=", Delta)

if Delta<0:
    print("Não existem raizes!")
else:
    X1= (-B + math.sqrt(Delta))/2*A
    X2= (-B - math.sqrt(Delta))/2*A
    print("X1=", X1)
    print("X2=", X2)
    
print("<<Fim>>")
