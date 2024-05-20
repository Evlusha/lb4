import random
import string
n = 12

def sorting1(arr, b, e):
    for i in range(b, e):
        for j in range(i + 1, e):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

def sorting2(arr, b, e):
    for i in range(b, e):
        for j in range(i + 1, e):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

def conect(arr1, arr2):
    for i in range(n):
        if i >= 0 and i <= 5:
            temp = arr1[i]
            arr1[i] = arr2[i + (n // 2)]
            arr2[i + (n // 2)] = temp
        else:
            temp = arr1[i]
            arr1[i] = arr2[i]
            arr2[i] = temp

def conclusion(arr):
    for i in range(n):
        print(arr[i], end=" ")

def sieveEratosthenes(numberProst):
    numberProst.append(2)
    for i in range(3, 30):
        k = 0
        for j in range(len(numberProst)):
            if (i % numberProst[j]) == 0:
                k += 1
        if k == 0:
            numberProst.append(i)

def examination(arr, numberProst):
    for i in range(n):
        for j in range(len(numberProst)):
            if arr[i] == numberProst[j]:
                print(arr[i], end=" ")

def repeat(arr1, arr2):
    j = 0
    x = [0, 0, 0, 0]
    for i in range(n):
        c = arr1[i]
        kol = 0
        while c > 0:
            x[kol] = c % 10
            c //= 10
            kol += 1
        counter = 0
        for z in range(3):
            for y in range(z + 1, 4):
                if x[z] == x[y]:
                    counter += 1
                    break
            if counter > 0:
                break
        if counter == 1:
            arr2[j] = arr1[i]
            j += 1
    return j

def Replacement(arr):
    for i in range(n):
        if arr[i] >= 'A' and arr[i] <= 'Z':
            arr[i] = chr(ord(arr[i]) + 32)
        elif arr[i] >= 'a' and arr[i] <= 'z':
            arr[i] = chr(ord(arr[i]) - 32)
            
def sieveEratosthenes(numberProst):
    # implementation of sieve of Eratosthenes
    pass

def examination(arr, numberProst):
    # implementation of examination function
    pass

def sorting1(arr, start, end):
    # implementation of sorting1 function
    pass

def sorting2(arr, start, end):
    # implementation of sorting2 function
    pass

def conect(arr1, arr2):
    # implementation of conect function
    pass

def Replacement(str):
    # implementation of Replacement function
    pass

def repeat(arr, newArr):
    # implementation of repeat function
    pass

def conclusion(arr):
    print(*arr)

arr1 = [0] * n
arr2 = [0] * n
ran = random.Random()
dist = random.randint(10, 100)

for i in range(n):
    arr1[i] = dist
    arr2[i] = dist

print("arr1: ", end="")
conclusion(arr1)
print("\narr2: ", end="")
conclusion(arr2)

print("\nПоиск простых элементов от 0-30: ")
numberProst = []
sieveEratosthenes(numberProst)

print("\narr1: ", end="")
examination(arr1, numberProst)
print("\narr2: ", end="")
examination(arr2, numberProst)

print("\nОтсортированные массивы: ")
sorting1(arr1, 0, n // 2)
sorting2(arr2, n // 2, n)

print("\narr1: ", end="")
conclusion(arr1)
print("\narr2: ", end="")
conclusion(arr2)

conect(arr1, arr2)

print("\nСмена отсортированных элементов: ")
print("\narr1: ", end="")
conclusion(arr1)
print("\narr2: ", end="")
conclusion(arr2)

str = [''] * n
rand1 = random.Random()
distr = random.randint(ord('A'), ord('z'))

for i in range(n):
    str[i] = chr(distr)

print("\nstr: ", end="")
for i in str:
    print(i, end=" ")

print("\n\nЗамена: ")
Replacement(str)

print("\nstr: ", end="")
for i in str:
    print(i, end=" ")

arr3 = [0] * n
sluch = random.Random()
dist_sl = random.randint(1000, 2000)

for i in range(n):
    arr3[i] = dist_sl

print("\n\narr3: ", end="")
conclusion(arr3)

sorting2(arr3, 0, n)

print("\nОтсортированный массив: ")
print("\narr3: ", end="")
conclusion(arr3)

newArr = [0] * n
k = repeat(arr3, newArr)

print("\nC повторяющимися цифрами: ")
print("\nnewArr: ", end="")
for i in range(k):
    print(newArr[i], end=" ")
