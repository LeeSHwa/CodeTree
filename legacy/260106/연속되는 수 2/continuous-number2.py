N = int(input())

count = 0
array = []

max_count = -1

for i in range(N):
    array.append(int(input()))
    if i == 0 or array[i] == array[i-1]:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 1

print(max_count)