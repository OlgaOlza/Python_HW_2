# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


N = int(input('Введите число N '))
P = 2
for i in range(N):
    P = P ** i
    if P <= N:
        print(P, end = ' ')
        P = 2
    else:
        print()
        break 