﻿/*
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

// Для понимания кода, сверяйтесь с прилагаемой в репозитории блок-схемой алгоритма в формате «drowio».

// Массивы, заданные в условии задачи:

string[] array1 = { "Hello", "2", "world", ":-)" };
string[] array2 = { "1234", "1567", "-2", "computer science" };
string[] array3 = { "Russia", "Denmark", "Kazan" };

// Сборка и вывод конечного массива из трёх или меньшего количества элементов:

void ThreeSymbols(string[] arrayIn)
{
    /*
Для сборки конечного массива создаётся временный массив, в который будут
собраны все строки с количеством символов меньше или равным трём. Размер временного
массива задаётся равным размеру входящего массива. Поскольку размер конечного
массива может отличаться от размера входящего массива, то вводим счётчик элементов,
чтобы впоследствии создать конечный массив из требуемых элементов.
*/

    string[] tempArray = new string[arrayIn.Length]; // временный массив
    uint elementCount = 0; // счётчик количества элементов конечного массива

    for (int i = 0; i < arrayIn.Length; i++)
    {
        if (arrayIn[i].Length <= 3) // если длина строки в пределах трёх символов
        {
            tempArray[elementCount] = arrayIn[i]; // заносим строку во временный массив
            elementCount++; // подсчитываем элемент, готовим следующую ячейку временного массива к приёму
        }
    }

    if (elementCount != 0) // если найдена хотя бы одна строка, удовлетворяющая заданному условию
    {
        string[] outArray = new string[elementCount]; // размер конечного массива
        // равен количеству занесённых во временный
        // массив элементов
        for (int i = 0; i < elementCount; i++)
            outArray[i] = tempArray[i]; // перенос собранных элементов в конечный массив

        Console.WriteLine("[\"{0}\"]", String.Join("\", \"", outArray)); // вывод собранного массива
    }
    else // если не найдена ни одна строка, удовлетворяющая заданному условию
        Console.WriteLine(
            "в заданном массиве отсутствуют элементы с меньшим "
                + "или равным 3-ём количеством символов."
        );
}

// Обработка примерных массивов, заданных в условии задачи:

void Examples(string[] arrayIn)
{
    Console.WriteLine("Исходный массив: [\"{0}\"].", String.Join("\", \"", arrayIn));
    Console.Write("Созданный массив: ");
    ThreeSymbols(arrayIn);
    Console.WriteLine();
}

Console.InputEncoding = Encoding.Unicode; // в консоли можно вводить символы Юникода, в т.ч. русские
ConsoleKeyInfo input; // переменная для получения кода клавиши
