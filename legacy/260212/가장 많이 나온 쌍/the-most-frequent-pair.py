n, m = map(int, input().split())

pairs = {}

for i in range(m):
    a, b = map(int, input().split())
    a, b = max(a, b), min(a, b)
    
    if (a, b) in pairs:
        pairs[(a, b)] += 1
    else: pairs[(a, b)] = 1
        
print(max(pairs.values()))
