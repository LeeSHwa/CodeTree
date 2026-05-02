X, Y = map(int, input().split())

# Please write your code here.

def cal(num):
    array = []

    while True:
        if num < 10:
            array.append(num)
            break

        rest = num % 10
        array.append(rest)
        num //= 10

    array = array[:: -1]

    return array

max_num = 0
for num in range(X, Y + 1):
    curr_num = sum(cal(num))

    max_num = max(max_num, curr_num)


print(max_num)