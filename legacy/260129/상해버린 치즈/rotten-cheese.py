from collections import defaultdict

N, M, D, S = map(int, input().split())

timeline1 = defaultdict(list)
timeline2 = defaultdict(list)

eat_mushroom = defaultdict(set)

for _ in range(D):
    p, m, t = map(int, input().split())
    timeline1[t].append((p, m))
    eat_mushroom[m].add(p)

for _ in range(S):
    p, t = map(int, input().split())
    timeline2[t].append(p)

candidates = set([i for i in range(1, M + 1)])

for time in range(1, 101):

    if timeline2[time]:                 # 만약 아팠다면 그 전의 먹은 사람과 버섯을 조사
        for person in timeline2[time]:

            current_cand = set()

            for in_time in range(1, time): # 아프기 전에 그 사람이 먹은 버섯을 후보에 추가

                if timeline1[in_time]:     # 만약 해당 시간에 누군가 먹은 흔적이 있다면

                    for p, m in timeline1[in_time]: # 먹은사람과 버섯을 순회하면서

                        if p == person:             # 만약 먹은사람이 아픈사람과 일치한다면
                            current_cand.add(m)     # 현재후보에 추가

            if len(current_cand):                           # 만약 현재 후보가 빈 값이 아니라면
                candidates = candidates & current_cand      # 기존 후보군들과 교집합 연산을 통해 용의자 버섯을 추림

max_med = 0

for candidate in candidates:
    curr_med = len(eat_mushroom[candidate])
    max_med = max(max_med, curr_med)

print(max_med)