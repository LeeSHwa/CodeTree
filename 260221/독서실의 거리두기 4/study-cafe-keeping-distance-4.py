N = int(input())
seats = list(map(int, input()))

def cal():
    dist = N

    for i in range(N - 1):
        for j in range(i + 1, N):
            if seats[i] == 1 and seats[j] == 1:
                dist = min(dist, j - i)            

    return dist

max_dist = 0

for i in range(N - 1):
    for j in range(i + 1, N):
        curr_dist = 0
        if seats[i] == 0 and seats[j] == 0:
            seats[i] = 1
            seats[j] = 1
            
            curr_dist = cal()

            max_dist = max(max_dist, curr_dist)

            seats[i] = 0
            seats[j] = 0

print(max_dist)        