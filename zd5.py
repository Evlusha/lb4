import random

# Инициализация таблиц
def initialize(S, K):
    s = len(S)
    for i in range(s):
        S[i] = i
    j = 0
    for i in range(s):
        j = (j + S[i] + K[i]) % s
        S[i], S[j] = S[j], S[i]

# Алгоритм псевдослучайной генерации
def generationAlgorithm(S, n):
    output = []
    i = 0
    j = 0
    for k in range(n):
        i = (i + 1) % n
        j = (j + S[i]) % n
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % n
        K = S[t]
        output.append(K)
    return output

if __name__ == "__main__":
    # 2^i
    n = 32
    S = [0] * n
    K = [i for i in range(n)]

    # Инициализация таблиц
    initialize(S, K)

    # Алгоритм псевдослучайной генерации
    output = generationAlgorithm(S, n)

    # Вывод сгенерированных чисел
    print("Сгенерированные числа:")
    for i in range(len(output)):
        print(f"{i+1}: {output[i]}")
