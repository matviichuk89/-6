import math
a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть h: "))
values = []
x=a 
while x<=b:
    y = math.e**x/(x**2+0.11)
    print(x, y)
    values.append(y)
    x=x+h
values.sort(reverse=True)
print(values)
