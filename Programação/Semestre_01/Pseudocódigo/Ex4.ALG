Algoritmo "semnome"
//  
//  
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 14/09/2023
Var
// Seção de Declarações das variáveis 
   valorTotalAserPago, valorDoQuiloWatt,quiloWatt: Real


Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreva(" Digite o valor dá media de kWh consumida: ")
       leia(valorDoQuiloWatt)
       quiloWatt <- 1.2
       valorTotalAserPago <- valorDoQuiloWatt * quiloWatt
       valorTotalAserPago <- valorTotalAserPago +  valorTotalAserPago * 0.18
       escreval(" Valor Total a ser pago: ", valorTotalAserPago )


Fimalgoritmo