import math
alpha = 1
while (alpha <= 5):
    z1 = ((1 - (2 * math.sin(alpha) * math.sin(alpha))) / (1 + math.sin(2 * alpha)))
    z2 = ((1 - math.tan(alpha)) / (1 + math.tan(alpha)))
    print("Значение альфа:", alpha)
    print("Значение z1", z1)
    print("Значение z2", z2)
    alpha = (alpha + 1)