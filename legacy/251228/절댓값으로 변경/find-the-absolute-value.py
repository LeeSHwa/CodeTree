def apply_abs(array):
    for i in range(len(array)):
        array[i] = abs(array[i])

N = int(input())
array = list(map(int, input().split()))

apply_abs(array)

for i in array:
    print(i, end = ' ')