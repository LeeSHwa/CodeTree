N = int(input())

class student:
    def __init__(self, name, sub1, sub2, sub3):
        self.name = name
        self.sub1 = int(sub1)
        self.sub2 = int(sub2)
        self.sub3 = int(sub3)

students = [student(*input().split()) for _ in range(N)]

students.sort(key=lambda x : (x.sub1 + x.sub2 + x.sub3))


for i in students:
    print(i.name, i.sub1, i.sub2, i.sub3)

