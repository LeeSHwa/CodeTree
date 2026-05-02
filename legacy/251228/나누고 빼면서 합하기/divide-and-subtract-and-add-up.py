N, M = map(int, input().split())
array = list(map(int, input().split()))

def calculator(array, index):
    sum_value = 0

    sum_value += array[index - 1] # 4
 
    while index > 1: # (4 -> 2), (2 -> 1)
        
        if index % 2 == 0:
            index //= 2
        else:
            index -= 1

        sum_value += array[index - 1] # 2, 1

    return sum_value

print(calculator(array, M))
            

    