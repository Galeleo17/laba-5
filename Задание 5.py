def example():
    a = int(input("Введите число a: "))
    b = int(input("Введите число b: "))
    c = (a + 4 * b) * (a - 3 * b) + a * 2
    return c

print(example())