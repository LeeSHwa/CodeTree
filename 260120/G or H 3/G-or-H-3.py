N, K = map(int, input().split())
position = [0] * 10001

max_pos = -1
for _ in range(N):
    pos, alaph = input().split()
    pos = int(pos)
    alaph = 1 if alaph == 'G' else 2

    position[pos] = alaph
    max_pos = max(max_pos, pos)

current_sum = sum(position[1 : K + 2]) # 1부터 K개의 구간을 넘어야 해서, 총 K + 1개의 지점을 포함
# print(current_sum)

sum_of_nums = [current_sum]
for i in range(1, max_pos - K):
    next_sum = current_sum - position[i] + position[i + K + 1]
    current_sum = next_sum
    sum_of_nums.append(next_sum)
    # print(f"i : {i}, sum : {next_sum}")

print(max(sum_of_nums))
