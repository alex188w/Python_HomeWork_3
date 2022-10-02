# 26.	Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов. Пример: для k = 8 
# список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

num = input("Введите натуральное число для вычисления чисел Фибоначчи : ")

if num.isdigit() == False:
    print('Введенное значение не походит для вычисления чисел Фибоначчи')
    exit()

num = int(num)

fib_pos = [1, 1]
fib1_1 = fib1_2 = 1
i = 2     
while i < num:
    fib_sum = fib1_2 + fib1_1
    fib1_1 = fib1_2
    fib1_2 = fib_sum
    i += 1
    fib_pos.append(fib_sum)   

fib_nega = [-1, 1]
fib2_1 = 1
fib2_2 = -1
i = 2    
while i < num:
    fib_sum = fib2_1 - fib2_2 
    fib2_1 = fib2_2
    fib2_2 = fib_sum
    i += 1
    fib_nega.insert(0, fib_sum)

fib_pos.insert(0, 0)
fib = fib_nega + fib_pos
print(f'Список чисел Фибоначчи, в том числе для отрицательных индексов, данного числа: \n {fib}')