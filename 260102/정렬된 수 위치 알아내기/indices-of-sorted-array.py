'''
입력을 받음   2 4 1 3 5
아래는 인덱스 1 2 3 4 5 

정렬시        1 2 3 4 5
             3 1 4 2 5

다시 돌려     2 4 1 3 5 
출력         2 4 1 3 5


'''

class Idx:
    count = 1
    def __init__(self, num):
        self.num = num
        self.count = Idx.count

        Idx.count += 1

n = int(input())

nums = list(map(int, input().split()))
idxs = []
for i in nums:
    idxs.append(Idx(i))

idxs.sort(key = lambda x: (x.num, x.count))

for i in range(n):
    idxs[i].num = i + 1
    
idxs.sort(key = lambda x: x.count)

for i in idxs:
    print(i.num, end = " ")