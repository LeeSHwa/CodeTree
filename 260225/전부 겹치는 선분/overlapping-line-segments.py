n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

is_duplicated = [0] * 101

for line in lines:
    start = line[0]
    end = line[1] + 1

    for idx in range(start, end):
        is_duplicated[idx] += 1
        if is_duplicated[idx] == n:
            print("Yes")
            exit()

print("No")
        
