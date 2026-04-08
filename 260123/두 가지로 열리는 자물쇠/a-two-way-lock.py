N = int(input())
nums = [i for i in range(1, N+1)]

a1, b1, c1 = map(int, input().split())

a2, b2, c2 = map(int, input().split())

def cal(temp):
    temp_range = [nums[(temp + num) % N] for num in range(-3, 2)]
    return temp_range

a1_range, b1_range, c1_range = cal(a1), cal(b1), cal(c1)
a2_range, b2_range, c2_range = cal(a2), cal(b2), cal(c2)
count = 0

for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if (i in a1_range and j in b1_range and k in c1_range) or (i in a2_range and j in b2_range and k in c2_range):
                # print(i, j, k, end = "/")
                count += 1


print(count)