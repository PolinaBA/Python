'''
Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
'''
a1 = int(input("Введите первый элемент арифметической прогрессии:  "))
d = int(input("Введите разность арифметической прогрессиии:  "))
n = int(input("Введите кол-во элементов арифметической прогрессии:  "))

from array import *
MyArray = array('i')
num = 0

for i in range(1,n + 1):
    num  = a1 + (i-1) * d
    MyArray.append(num)
print(MyArray)






