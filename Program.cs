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
    for (int i=0; i < arrayN.Length; i++)
        Console.WriteLine(arrayN[i]);
}

Console.InputEncoding=Encoding.Unicode;
string s=Console.ReadLine();
Console.WriteLine(s);
PrintArray(array3);