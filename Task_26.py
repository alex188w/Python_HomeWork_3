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
fib_nega = [-1, 1]
fib_pos = [1, 1]

def pos_fib(n):
    fib1 = fib2 = 1
    i = 2    
    
    while i < n:
        fib_sum = fib2 + fib1
        fib1 = fib2
        fib2 = fib_sum
        i += 1
        fib_pos.append(fib_sum)
    return fib_sum 

def nega_fib(n):    
    fib1 = 1
    fib2 = - 1
    i = 2    
    
    while i < n:
        fib_sum = fib1 - fib2 
        fib1 = fib2
        fib2 = fib_sum
        i += 1
        fib_nega.insert(0, fib_sum)
    return fib_sum 
    
pos_fib(num)
nega_fib(num)

fib_pos.insert(0, 0)
fib = fib_nega + fib_pos
print(f'Список чисел Фибоначчи, в том числе для отрицательных индексов, данного числа: \n {fib}')