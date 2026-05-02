n = int(input())
arr = list(map(int, input().split()))

def cal(index):
    
    if index == 0:
        return arr[0]
    
    return max(cal(index-1), arr[index])

print(cal(n - 1))