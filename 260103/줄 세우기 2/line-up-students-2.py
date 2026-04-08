class student:
    count = 1

    def __init__(self, hei, wei):
        self.hei = hei
        self.wei = wei

        self.no = student.count

        student.count += 1

n = int(input())

students = [student(*map(int, input().split())) for _ in range(n)]

students.sort(key = lambda x : (x.hei, -x.wei))

for i in students:
    print(i.hei, i.wei, i.no)