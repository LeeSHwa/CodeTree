x = int(input())

def find_max_velocity(x):

    curr_sum = 0
    last_sum = 0

    for i in range(1, x):
        curr_sum += i
        
        if x - curr_sum < last_sum:
            return i - 1
        elif last_sum <= x - curr_sum <= curr_sum:
            return i

        last_sum = curr_sum

max_velocity = find_max_velocity(x)
curr_velocity = max_velocity

second = max_velocity
distance = x - sum(range(max_velocity + 1))

while curr_velocity != 1:
    rest_distance = sum(range(curr_velocity))     # 유지하지 않고 쭉 내릴 경우
    if distance - rest_distance >= curr_velocity: # (만약 남은거리) - (쭉 내릴 경우)가 현재 속도보다 크다면
        distance -= curr_velocity                 # 남은거리에서 현재 속도를 빼주고
        second += 1                               # 1초 증가
    
    else:
        curr_velocity -= 1

print(distance + second)