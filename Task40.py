'''
Подсчет элементов которые стоят между большими числами 
'''
from random import randint as rnd

N = int(input('Введите количество элементов списка: '))
list1 = [rnd(1,10) for _ in range(N)]
print(list1)

def minbetween(list1):
    count = 0
    for i in range(N-2):
        if list1[i] > list1[i+1] < list1[i+2]:
            count+=1
    print (count)

minbetween(list1)                  