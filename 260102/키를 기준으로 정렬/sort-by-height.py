n = int(input())

array = []

for _ in range(n):
    array.append(tuple(input().split()))

array.sort(key = lambda x : x[1])

for i, j, k in array:
    print(i, j, k)