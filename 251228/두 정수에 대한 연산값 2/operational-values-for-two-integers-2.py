def calculate_magic_num(a, b):
    if a > b:
        return a * 2, b + 10
    else:
        return a + 10, b * 2

a, b = map(int, input().split())
a, b = calculate_magic_num(a, b)
print(a, b)
