N, M = map(int, input().split())

arr = list(map(int, input().split()))

def sum_of_range(start, end):
    global arr
    
    return sum(arr[start - 1 : end])


for _ in range(M):
    start, end = map(int, input().split())
    
    print(sum_of_range(start, end))