class Distance():
    no = 1
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.distance = abs(x) + abs(y)
        self.no = Distance.no

        Distance.no += 1

N = int(input())

pos = [Distance(*map(int, input().split())) for _ in range(N)]

pos.sort(key = lambda x: (x.distance, x.no))

for i in pos:
    print(i.no)