N = int(input())

class student:
    count = 1

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

        self.No = student.count

        student.count += 1
    
    
students = [student(*map(int, input().split())) for _ in range(N)]

students.sort(key = lambda x: (-x.height, -x.weight, x.No))

for student in students:
    print(student.height, student.weight, student.No)
    