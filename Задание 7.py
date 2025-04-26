import math

x = float(input("x = "))
y = float(input("y = "))
radius = float(input("radius = "))
belongs = math.sqrt(x ** 2 + y ** 2)
if belongs <= radius:
    print("Точка принадлежит кругу")
else:
    print("Точка не принадлежит кругу")