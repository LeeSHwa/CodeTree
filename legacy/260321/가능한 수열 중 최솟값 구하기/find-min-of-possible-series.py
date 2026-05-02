n = int(input())

array = [4, 5, 4, 6] * 20

print(''.join(map(str, array[:n])))