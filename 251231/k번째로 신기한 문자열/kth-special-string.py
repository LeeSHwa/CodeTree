N, K, T = input().split()
N = int(N)
K = int(K)

start_with_T = []
window = len(T)

for _ in range(N):
    word = input()
    if word[:window] == T:
        start_with_T.append(word)

start_with_T.sort()

print(start_with_T[K-1])