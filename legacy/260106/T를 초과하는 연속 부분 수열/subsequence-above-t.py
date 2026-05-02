N, T = map(int, input().split())

array = list(map(int, input().split()))
count = 0
max_count = 0

for i in range(N):
    
    if array[i] > T:
        count += 1
    else:
        count = 0
        
    max_count = max(max_count, count)
    
print(max_count)