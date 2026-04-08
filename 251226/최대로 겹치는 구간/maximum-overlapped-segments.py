''' 
겹치는 구간의 경우에는, 지점이 아니기 때문에 시작점의 위치만 기록하면 된다.
그래서 (2, 5)의 경우는 2~3, 3~4, 4~5가 있을 것이고
(4, 6) 같은 경우는 4~5, 5~6 이 있을 것인데

이렇게 된다면 겹치는 지점은 4와 5로 총 2개지만
겹치는 '구간'은 4~5로 한 개이다. 

음수의 경우에는 offset을 두어서, 크기만큼 항상 +를 시켜준다.
because why -> 배열에는 음수를 사용할 수 없다.
'''

N = int(input())

line = [0] * 300 # 넉넉하게
offset = 100
max_duplicated = -1

for _ in range(N):
    start, end = map(int, input().split())
    start += offset
    end += offset

    for i in range(start, end): # end-1까지만 표시
        line[i] += 1

    max_duplicated = max(max_duplicated, max(line))

# count = 0
# for i in line:
#     if i == max_duplicated:
#         count += 1

# print(count)

print(max_duplicated)