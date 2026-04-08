X, Y = map(int, input().split())

# Please write your code here.

cnt = 0
for num in range(X, Y + 1):
    array = list(map(int, str(num)))
    set_array = set(array)

    if len(set_array) == 2:
        a, b = set_array
        len_array = len(array)

        a_count = array.count(a)
        b_count = len(array) - a_count

        if a_count > 1 and b_count > 1:
            continue
    
        cnt += 1
        
print(cnt)