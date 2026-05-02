import itertools

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if M > N:
    print(0)
    exit()

# buti = list(set(itertools.permutations(B, M)))

start = 0
end = M
count = 0

sorted_B = sorted(B)


for _ in range(N - M + 1): # 8 - 3
    window = sorted(A[start:end])

    if window == sorted_B:
        count += 1

    start += 1
    end += 1

print(count)