n, m = map(int, input().split())

array = []

def is_possible(num):
    if num in array or (len(array) > 0 and array[-1] > num):
        return False
    return True

def backtrack(depth):
    if depth == m:
        print(*array)
        return
    
    for i in range(1, n + 1):
        if is_possible(i):
            array.append(i)
            backtrack(depth + 1)
            array.pop()

backtrack(0)