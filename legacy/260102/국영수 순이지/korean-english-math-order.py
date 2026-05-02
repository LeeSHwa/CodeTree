class score:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = int(kor)
        self.eng = int(eng)
        self.math = int(math)


n = int(input())
scores = []

for _ in range(n):
    scores.append(score(*input().split()))

scores.sort(key = lambda x : (x.kor, x.eng, x.math), reverse = True)

for i in scores:
    print(i.name, i.kor, i.eng, i.math)