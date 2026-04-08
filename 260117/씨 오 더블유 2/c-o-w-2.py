N = int(input())

array = list(input())

C_count = 0
CO_count = 0
COW_count = 0

ans = 0

for i in range(N):

    if array[i] == 'C':
        C_count += 1
        
    
    if array[i] == 'O':
        CO_count += C_count
    
    if array[i] == 'W':
        COW_count += CO_count

print(COW_count)