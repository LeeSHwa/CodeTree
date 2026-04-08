N = int(input())

position = [0] * 101

min_pos = 101
max_pos = -1

for _ in range(N):
    pos, flag = input().split()
    pos = int(pos)
    
    position[pos] = flag
    min_pos, max_pos = min(min_pos, pos), max(max_pos, pos)

max_len = 0

for start in range(min_pos, max_pos + 1):
    for end in range(start + 1, max_pos + 1):
        
        if not position[start] or not position[end]:
            continue
        
        G = position[start:end + 1].count("G")
        H = position[start:end + 1].count("H")
        
        if G == H or (G and not H) or (not G and H):
            curr_len = end - start
        
        max_len = max(max_len, curr_len)

print(max_len)
        