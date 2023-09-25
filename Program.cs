/*
Задача: Написать программу, которая из имеющегося массива строк формирует
новый массив из строк, длина которых меньше, либо равна 3 символам.
Первоначальный массив можно ввести с клавиатуры, либо задать на старте
выполнения алгоритма. При решении не рекомендуется пользоваться коллекциями,
лучше обойтись исключительно массивами.

Примеры:
[“Hello”, “2”, “world”, “:-)”] > [“2”, “:-)”]
[“1234”, “1567”, “-2”, “computer science”] > [“-2”]
[“Russia”, “Denmark”, “Kazan”] > []
*/


using System;
using System.Text;

string[] array1 = { "Hello", "2", "world", ":-)" };
string[] array2 = { "1234", "1567", "-2", "computer science" };
string[] array3 = { "Russia", "Denmark", "Kazan" };

void PrintArray(string[] arrayN)
{
    Console.Write("[\"");
    for (int i=0; i < arrayN.Length-1; i++)
        Console.Write($"{arrayN[i]}\", \"");
    Console.WriteLine($"{arrayN[arrayN.Length-1]}\"]");
}

Console.InputEncoding=Encoding.Unicode;

PrintArray(array1);