'''
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
'''

N = int(input("Введите кол-во монеток: "))
i = 1
countR = 0
countG= 0
while i <= N :
    s = int(input(f"Введите сторону монетки № {i}(решка - 1, герб - 0): "))
    
    if s == 1 :
        countR += 1
    else :
        countG += 1
    i += 1

if countR >= countG :
    print((f"Минимальное число монеток, которое нужно перевернуть:{countG}"))
else :
    print((f"Минимальное число монеток, которое нужно перевернуть:{countR}"))



