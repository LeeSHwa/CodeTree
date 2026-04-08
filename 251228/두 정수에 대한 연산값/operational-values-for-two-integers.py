def calculate_magic_num(a, b):
    if a > b:
        return a + 25, b * 2
    else:
        return a * 2, b + 25

a, b = map(int, input().split())
a, b = calculate_magic_num(a, b)
print(a, b)
