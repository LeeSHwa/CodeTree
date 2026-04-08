n = int(input())

seats = list(input())

max_distance = 0
candidate = -1

last_idx = 0
for i in range(1, n):
    if seats[i] == '1':
        
        if i - last_idx > max_distance:
            max_distance = i - last_idx
            candidate = (i + last_idx) // 2      
         
        last_idx = i

seats[candidate] = '1'


min_distance = float('inf')

last_idx = 0
for i in range(1, n):
    if seats[i] == '1':
        curr_distance = i - last_idx
        min_distance = min(min_distance, curr_distance)

        last_idx = i

print(min_distance)