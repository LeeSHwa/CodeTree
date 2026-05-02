# 3 5 1 4 2
# (3, 1), (4, 2), 5
# 팀 점수가 같으면 안됨
# 이번엔 완탐으로 접근

devs = list(map(int, input().split()))

devs.sort() # 일단 정렬을 해

min_diff = 2001

for i in range(4):
    for j in range(i + 1, 5):
        team1 = devs[i] + devs[j]

        for k in range(4):
            for l in range(k + 1, 5):
                
                if k != i and l != j and k != j and l != i:
                    team2 = devs[k] + devs[l]

                    team3 = sum(devs) - team1 - team2
                
                    if team3 != team2 and team2 != team1:
                        diff = max(team1, team2, team3) - min(team1, team2, team3)

                        min_diff = min(min_diff, diff)

if min_diff == 2001:
    print(-1)
else: print(min_diff)