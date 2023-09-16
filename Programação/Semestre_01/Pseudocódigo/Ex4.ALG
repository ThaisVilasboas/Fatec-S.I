Algoritmo "exercicio 4"
//  
//  
// Descrição   : Calcular o valor a ser pago de energia elétrica sabendo-se que o valor a pagar por quilowatt é de R$0.12
//                 apresentar o valor total a ser pago pelo usuário acrescido de 18% de ICMS.
// Autor(a)    : Thais Vilasboas
// Data atual  : 14/09/2023
Var
// Seção de Declarações das variáveis 
   valorTotalAserPago, valorDoQuiloWatt,quiloWatt: Real


Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreva(" Digite o valor dá media de kWh consumida: ")
       leia(valorDoQuiloWatt)
       quiloWatt <- 0.12
       valorTotalAserPago <- valorDoQuiloWatt * quiloWatt
       valorTotalAserPago <- valorTotalAserPago +  valorTotalAserPago * 0.18
       escreval(" Valor Total a ser pago: ", valorTotalAserPago )


Fimalgoritmo
