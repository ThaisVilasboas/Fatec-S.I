using System;

namespace Aula001
{
    internal class Program
    {
        static void Main(string[] args)
        {
            float Nota1 = 0, Nota2 = 0, Media = 0;

            Console.Write($"Digite o valor da sua primeira nota: "); 
            Nota1 = float.Parse(Console.ReadLine());

            Console.Write($"Digite o valor da sua segunda nota: ");
            Nota2 = float.Parse(Console.ReadLine());

            Media = (Nota1 + Nota2) / 2;
            Console.Write($"Sua média final é:{Media} ");
            
            Console.ReadKey();
        }
    }
}
