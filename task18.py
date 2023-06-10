# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*
# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input("Введите кол-во элементов: "))
lst = []
for i in range(n):
    numbers = int(input("Введите числа массива: "))
    lst.append(numbers)
x = int(input("Введите своё число: "))

index_element = 0
min_element = abs(x - lst[0])
for i in range(1, n):
    buffer_element = abs(x -lst[i])
    if buffer_element < min_element:
        min_element = buffer_element
        index_element = i

print(f"Самый близкий по величине элемент к заданному числу {lst[index_element]}")