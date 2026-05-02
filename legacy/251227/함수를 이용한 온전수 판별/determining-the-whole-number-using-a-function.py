def find_magic_num(A, B):
    count = 0

    for num in range(A, B+1):
        if num % 2 == 0:
            continue
        
        if num % 10 == 5:
            continue

        if num % 3 == 0 and num % 9 != 0:
            continue
        
        else:
            count += 1
    return count

A, B = map(int, input().split())
print(find_magic_num(A, B))
