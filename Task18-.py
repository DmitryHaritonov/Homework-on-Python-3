#Задача 18:
#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
#Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
#Заполните массив случайными натуральными числами от 1 до N.
#Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.

#Ввод: 10
#Ввод: 7
#1 2 1 8 9 6 5 4 3 4
#Вывод: 6


n = int(input())
list_1 = list()
for i in range(n):
    x = int(input())
    list_1.append(x)

k = int(input())
m = abs(k - list_1[0])

Figure = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        Figure = list_1[i]
print(Figure)