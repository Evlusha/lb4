import math

E = 0.0001

def f(x):
    return (2 * x) + math.cos(x) - 0

def f1(x):
    return 2 - math.sin(x) - 0

def halfDivision(a, b, roots):
    if f(a) * f(b) >= 0.0:
        print("Неверный интервал")
        return 0
    
    k = 0
    c = 0
    while abs(b - a) >= E:
        print(f"{k:7d}|{a:8.4f} | {b:8.4f}|{b - a}")
        c = (a + b) / 2
        if f(c) == 0.0:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        k += 1
    
    roots.append(c)
    print(f"Корень {c} с {k} итерациями")
    return k

def newtonMethod(x0, roots):
    k = 0
    x1 = x0 - f(x0) / f1(x0)
    while abs(x1 - x0) >= E:
        print(f"{k:7d}|{x0:8.4f} | {x1:8.4f}|{x1 - x0}")
        x0 = x1
        x1 = x0 - f(x0) / f1(x0)
        k += 1
    
    roots.append(x0)
    print(f"Корень {x0} с {k} итерациями")
    return k

def simpleIterations(x0, roots):
    k = 0
    x1 = 1 / math.log(x0 + 1)
    while abs(x1 - x0) > E:
        print(f"{k:7d}|{x0:8.4f} | {x1:8.4f}|{x1 - x0}")
        x0 = x1
        x1 = 1 / math.log(x0 + 1)
        k += 1
    
    roots.append(x0)
    print(f"Корень {x0} с {k} итерациями")
    return k

if __name__ == "__main__":
    print("программу уточнения корня методом половинного деления с точностью до E")
    roots = []
    s1 = halfDivision(-1, 1, roots)
    
    print("\nпрограмму уточнения корня Ньютоном с точностью до E")
    s2 = newtonMethod(10, roots)
    
    print("\nметода простых итераций")
    s3 = simpleIterations(2, roots)
    
    print("\nвсе корни уравнения")
    for i in roots:
        print(i, end=" ")
    
    print("\nСкорость сходимости:")
    print("\nУ Ньютона итераций", s2)
    print("\nУ метода простых итераций ", s3)
    print("\nУ  методом половинного деления ", s1)
    
