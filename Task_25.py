# 25.	Напишите программу, которая будет преобразовывать десятичное число 
# в двоичное. Пример: 45 -> 101101 3 -> 11 2 -> 10

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

num = input("Введите натуральное число для перевода: ")

if num.isdigit() == False:
    print('Введенное значение не может быть переведено')
    exit()

num = int(num)

print(bin(num)[2:]) # Вывод строки со втрого элемента

print(int(bin(num)[2:])) # Вывод преобразованием в число

exit()
remain = ''
while num > 0:
    remain = str(num % 2) + remain
    num = num // 2
    
print(f'Заданное число в двоичном коде: {remain}')

