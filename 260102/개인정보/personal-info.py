class User():
    def __init__(self, name, hei, wei):
        self.name = name
        self.hei = int(hei)
        self.wei = float(wei)

users = [User(*input().split()) for _ in range(5)]

sorted_by_name = sorted(users, key = lambda x : x.name)
sorted_by_hei = sorted(users, key = lambda x : -x.hei)

print("name")
for i in sorted_by_name:
    print(i.name, i.hei, i.wei)

print()

print("height")
for hei in sorted_by_hei:
    print(hei.name, hei.hei, hei.wei)
