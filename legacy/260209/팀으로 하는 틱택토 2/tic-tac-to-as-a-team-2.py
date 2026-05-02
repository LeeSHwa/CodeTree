nums = [str(input()) for _ in range(3)]

ans = []


# 1. 가로 3줄
for i in range(3):
    set_num = set()

    set_num.add(nums[i][0])
    set_num.add(nums[i][1])
    set_num.add(nums[i][2])


    if len(set_num) == 2 and not set_num in ans:
        ans.append(set_num)



# 2. 세로 3줄
for i in range(3):
    set_num = set()

    set_num.add(nums[0][i])
    set_num.add(nums[1][i])
    set_num.add(nums[2][i])

    if len(set_num) == 2 and not set_num in ans:
        ans.append(set_num)


set_num = set()

# 3. 대각선 (좌상 -> 우하)
for i in range(3):
    set_num.add(nums[i][i])

if len(set_num) == 2 and not set_num in ans:
    ans.append(set_num)

set_num = set()

# 4. 대각선 (우상 -> 좌하)
for i in range(3):
    set_num.add(nums[i][2 - i])

if len(set_num) == 2 and not set_num in ans:
    ans.append(set_num)

print(len(ans))