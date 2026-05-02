from collections import deque

n = int(input())

def solve():
    
    q = deque()
    q.append((n, 0))
    visited = set()

    while q:
        num, cnt = q.popleft()
        
        if num == 1:
            return cnt
        
        nums = []
        nums.append(num + 1)
        nums.append(num - 1)
        if num % 2 == 0: nums.append(num // 2)
        if num % 3 == 0: nums.append(num // 3)

        for elem in nums:
            if elem not in visited:
                visited.add(elem)
                q.append((elem, cnt + 1))
    

        

print(solve())