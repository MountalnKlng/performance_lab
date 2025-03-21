﻿# Performance_lab

Тестовое задание из четырех этапов. 
Решения были сделаны из соображений экономии времени и памяти.

Первая задача могла быть решена через добавление шага к общей строчке, которая потом 
бы выводилась, или же с помощью использования массивов. В финальной реализации, которая этого не включает,
скорость вывода ответа по большей части ограничена лишь командой print.

Вторая задача изначально была сделана с помощью функции, которая бы вычисляла,
является ли точка частью окружности или нет, однако в подобном разделении
по итогу не было нужды, поскольку сама программа после оптимизации вышла достаточно
короткой.

Третья задача требует рекурсии, поскольку в файле task.json может быть потенциально
огромное множество подуровней. Каждый из них находится под ключом "values" более высокого
уровня, что позволяет свести задачу к рекурсивному проходу по всему файлу, и здесь
для этого уже потребуется функция, которая будет вызывать сама себя.

Четвертая задача подразумевала решение, использующее массив. Итоговое значение,
к которому нужно было бы привести все значения, это медиана. Среднее арифметическое 
дает неверные значения там, где не совпадает с медианой, например массив [1, 1, 1, 10, 1],
где правильный ответ 9, но при использовании среднего арифметического, числа приравниваются не к 1, а к 3,
что дает ответ 15.

В последних трех задачах в папках также лежат файлы, на которых проверялась корректность
работы алгоритмов. 
