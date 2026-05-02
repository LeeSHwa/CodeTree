n = int(input())
array = []

def is_possible(idx):
    
    for i in range(1, (idx + 1) // 2 + 1):
        if i == 1 and array[-1] == array[-2]:
            return False
        else:
            flag = True
            for search in range(0, i):
                if array[- (i * 2) + search] != array[-i + search]:
                    flag = False
            if flag:
                return False

    return True
    

def backtrack(idx):

    if idx == n:
        print(''.join(map(str, array)))
        exit()
    
    for num in range(4, 7):
        array.append(num)
        if is_possible(idx):
            backtrack(idx + 1)
        array.pop()
    
        
backtrack(0)