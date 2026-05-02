n = int(input())

last_pos = {}



ans = 0

for i in range(n):

    googoo, side = map(int, input().split())

    if googoo in last_pos and side != last_pos[googoo]:

        ans += 1
    
    last_pos[googoo] = side



print(ans)