N = int(input())

array = [int(input()) for _ in range(N)]
count = 1
max_count = 1

for i in range(N):
    if i == 0:
        continue
    
    if array[i] * array[i-1] >= 0:
        count += 1
    else:
        count = 1
        
    max_count = max(max_count, count)
    
print(max_count)