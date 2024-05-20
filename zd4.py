import random

def algorithm1(round_number, own, enemy):
    if round_number == 0:
        own.append(1)
    else:
        own.append(0)

def algorithm2(round_number, own, enemy):
    own.append(random.randint(0, 1))

def algorithm3(round_number, own, enemy):
    if len(own) > 0 and not enemy[len(own) - 1]:
        own.append(1)
    else:
        own.append(0)

if __name__ == "__main__":
    n = random.randint(100, 200)
    first = []
    second = []
    check1 = 0
    check2 = 0

    for i in range(n):
        algorithm3(i, first, second)
        algorithm2(i, second, first)

        if first[i] and second[i]:
            check1 += 24
            check2 += 24
        elif first[i] and not second[i]:
            check1 += 0
            check2 += 20
        elif not first[i] and second[i]:
            check1 += 20
            check2 += 0
        elif not first[i] and not second[i]:
            check1 += 4
            check2 += 4

        print(first[i], second[i], check1, check2)
