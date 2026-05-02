class User():
    def __init__(self, name, hei, wei):
        self.name = name
        self.hei = int(hei)
        self.wei = int(wei)

n = int(input())
users = [User(*input().split()) for _ in range(n)]

sorted_user = sorted(users, key = lambda x : (x.hei, -x.wei))


for i in sorted_user:
    print(i.name, i.hei, i.wei)
