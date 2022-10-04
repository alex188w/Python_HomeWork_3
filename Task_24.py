# 24.	Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

import random
my_list = []

for i in range(5):
    num = random.random() * 100 
    my_list.append(round(num, 2))
    
print(f'Заданный сисок: {my_list}')

my_list = [round(val % 1, 2) for val in my_list]
print(f'Заданный сисок: {my_list}')
rev_result = max(my_list) - min(my_list)
print(f'Разница между значеними :  {rev_result:.2f}')

exit()
max_i = 0
min_i = 0.99

for i in range(5):
    temp = abs(my_list[i]) % 1    
    if temp > max_i:
        max_i = temp
        
for i in range(5):
    temp = abs(my_list[i]) % 1 
    if temp < min_i:
        min_i = temp        

print(f'Максимальное значение дробной части элементов составляет: {round((max_i), 2)}')
print(f'Минимаотное значение дробной части элементов составляет: {round((min_i), 2)}')
print(f'Разница между значеними : {round((max_i), 2) - round((min_i), 2)}')
