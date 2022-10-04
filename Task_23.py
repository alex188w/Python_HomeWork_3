# 23.	Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

len_sp = input("Введите длину списка с чмслами: ")

if len_sp.isdigit() == False:
    print('Введенное значение не может являться длиной списка')
    exit()

my_list = []
len_sp = int(len_sp)

import random
for i in range(len_sp):
    num = random.randint(0, 9)
    my_list.append(num)

print(f'Заданный сисок: {my_list}')

my_list_mult = []
mult_p = 1

if len_sp % 2 == 0:
    for i in range(len_sp // 2):
        mult_p = my_list[i] * my_list[len_sp - 1 - i]      
        my_list_mult.append(mult_p)
        
else:
    for i in range(len_sp // 2 + 1):
        mult_p = my_list[i] * my_list[len_sp - 1 - i]      
        my_list_mult.append(mult_p)
    # elem = my_list[len_sp // 2]**2
    # my_list_mult.append(elem)

print(f'Призведение пар чисел исходного списка: {my_list_mult}')
