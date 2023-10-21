#7) A prefeitura de Araraquara cobra o valor do IPTU de acordo com a área em que está situado o imóvel. Para
#calcular o valor do IPTU são digitados os seguintes dados: 
#- Área do imóvel ( em m2);
#- O Valor m2 para cada tipo de imóvel é dado conforme
#a tabela abaixo:
#1 – Residencial, preço por m2 = R$ 2,00
#2 – Comercial, preço por m2 = R$ 4,00
#3 – Industrial, preço por m2 = R$ 5,00
#Escreva um programa em C que calcule e mostre o valordo IPTU de acordo com o tipo de imóvel.




area= float(input("Digite a área do imóvel:"))
tipoImovel= int(input("Digite o tipo de imóvel:\n1-Residencial\n2-Comercial\n3-Industrial\n"))
if tipoImovel ==1:
    valorDoIPTU= area*2
elif tipoImovel ==2:
    valorDoIPTU= area*4
else :
    valorDoIPTU= area*5
print ("Valor do IPTU: R$", valorDoIPTU)

