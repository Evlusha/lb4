import random

n1 = 50
n2 = 100
n3 = 1000

def filling(arr, n):
    for i in range(n):
        arr[i] = random.randint(1, 100)

def X2(arr, n):
    iter = 25
    sum = [0] * iter
    mat = 0
    for i in range(n):
        sum[arr[i] * iter // 101] += 1
        mat += arr[i]
    
    x = 0
    print("Кол-во i элементов в 25 интервалах")
    for i in sum:
        print(i, end=" ")
        x += ((i - (n // iter)) ** 2) / (n // iter)
    
    print("\nМат ожидание ожидание: 50,5 реальность:", mat / n)
    return x

if __name__ == "__main__":
    arr1 = [0] * n1
    filling(arr1, n1)
    arr2 = [0] * n2
    filling(arr2, n2)
    arr3 = [0] * n3
    filling(arr3, n3)
    
    krit = 44.314
    print("Для массива на 50 элементов")
    x = X2(arr1, n1)
    print("x^2:", x)
    if x < krit:
        print("Гипотеза о нормальном распределении принимается.")
    else:
        print("Гипотеза о нормальном распределении отклоняется.")
    
    print("Для массива на 100 элементов")
    x = X2(arr2, n2)
    print("x^2:", x)
    if x < krit:
        print("Гипотеза о нормальном распределении принимается.")
    else:
        print("Гипотеза о нормальном распределении отклоняется.")
    
    print("Для массива на 1000 элементов")
    x = X2(arr3, n3)
    print("x^2:", x)
    if x < krit:
        print("Гипотеза о нормальном распределении принимается.")
    else:
        print("Гипотеза о нормальном распределении отклоняется.")
