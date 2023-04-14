'''
ВВывести элементы первого массива которы нет во втором массиве
'''
N = int(input('Введите количество элементов 1го массива: '))
M = int(input('Введите количество элементов 2го массива: '))

list1 = list(range(N))
list2 = []

for i in range(N):
    x = int(input(f'Введите {list1[i]+1} элемент 1го массива: '))
    list1.pop(0)
    list1.append(x)
    
for i in range(M):
    list2.append(int(input(f'Введите {i+1} элемент 2го массива: ')))

print(f'1ый массив: {list1}')
print(f'2ой массив: {list2}')

list3 = []
for i in list1:
    if i not in list2:
        list3.append(i)

print(list3)