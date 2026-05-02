N = int(input())
cows = list(map(int, input().split()))

count = 0

for first in range(N-2):
    for second in range(first + 1, N-1):
        for thrid in range(second + 1, N):
            if cows[first] <= cows[second] and cows[second] <= cows[thrid]:
                count += 1
        

print(count)