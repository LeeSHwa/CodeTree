N = int(input())

array = list(map(int, input().split()))
temp = []

for i in range(N):
    temp.append(array[i])

    if i % 2 == 0:
        temp.sort()
        print(temp[i // 2], end = " ")