import math
alpha = int(input("Введите значение альфа:"))
z1 = ((1 - (2 * math.sin(alpha) * math.sin(alpha))) / (1 + math.sin(2 * alpha)))
z2 = ((1 - math.tan(alpha)) / (1 + math.tan(alpha)))
print("Значение z1", z1)
print("Значение z2", z2)