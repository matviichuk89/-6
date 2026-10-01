import math
a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть h: "))
values = []
n = int((b - a) / h)
for i in range(n+1):
    x = a + i * h
    y = math.e**x/(x**2+0.11)
    print(x, y)
    values.append(y)
    values.sort(reverse=True)
    print(values)