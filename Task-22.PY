# Задача 22.	Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

my_list = []
sum_n = 0
for i in range(5):
    num = random.randint(0, 99) 
    my_list.append(num)
    # if i % 2 != 0:
    #     sum_n += my_list[i]

print(f'Заданный сисок: {my_list}')
print(f'Сумма элементов на нечетных позициях: {sum(my_list[1::2])}')
