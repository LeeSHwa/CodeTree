from collections import defaultdict

n, m = map(int, input().split())
height_dict = defaultdict(list)

ladders = [tuple(map(int, input().split())) for _ in range(m)]


# 진짜 간단하게 그냥 1을 넣었을 때, 1이 사다리 타고 어디로 가는지 계산하는 함수
# ladders.values()를 오름차순 sort()하여 내가 있는 depth에 혹시 num - 1 or num이 있는지 확인
# num이 있다면 num의 pos는 -1
# num - 1이 있다면 num의 pos는 +1

# 그래서 최종 pos를 저장해야지
# 그럼 그냥 for문으로 가능하지 않나?? 굳이 depth 관리해가며 재귀를 써야할 이유가?

for width, height in ladders:
    height_dict[height].append(width)

position = [0] * (n + 1)

for man in range(1, n + 1):
    curr = man
    
    for pos in range(1, 16):
    
        if curr in height_dict[pos]: # 현재 위치에 오른쪽으로 가로줄이 있다면
            curr += 1                # + 1

        elif curr - 1 > 0 and curr - 1 in height_dict[pos]: # 현재 위치에 왼쪽으로 가로줄이 있다면
            curr -= 1                                       # -1
        else:
            continue
    position[curr] = man

ans = 0
for temp, num in enumerate(position[1:]):
    idx = temp + 1
    
    if num - idx < 0:
        ans -= num - idx

print(ans)