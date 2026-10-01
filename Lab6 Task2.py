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
print(values)
values.sort(reverse=True)
middle = len(values) // 2

if len(values) % 2 == 0:
    list1 = values[:middle]
    list2 = values[middle:]
else:
    list1 = values[:middle]
    list2 = values[middle + 1:]

print(list1)
print(list2)