n = int(input())
array = []
cnt = 0
# Please write your code here.
def is_beauti(nums):
    idx = 0
    while idx < n:
    
        stack = int(nums[idx])
    
        for i in range(1, stack): 
            if idx + i >= n or nums[idx + i] != nums[idx]:
                return 0
        
        idx += stack
    
    return 1


def recurr(depth):
    global cnt
    if depth == n:
        temp = ''.join(map(str, array))
        cnt += is_beauti(temp)
        return
    
    for num in range(1, 5):
        array.append(num)
        recurr(depth + 1)
        array.pop()

ans = recurr(0)
print(cnt)