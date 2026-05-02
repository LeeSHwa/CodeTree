devs = list(map(int, input().split()))
N = len(devs)

all_sum = sum(devs)
min_diff = float('inf')

for i in range(N - 2):
    for j in range(i+1, N - 1):
        for k in range(j + 1, N):
            curr_sum = devs[i] + devs[j] + devs[k]

            min_diff = min(min_diff, abs(all_sum - curr_sum * 2))

print(min_diff)