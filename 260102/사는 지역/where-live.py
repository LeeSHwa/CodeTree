class location:
    def __init__(self, name, num, loc):
        self.name = name
        self.num = num
        self.loc = loc

locations = []
n = int(input())
for _ in range(n):
    locations.append(location(*input().split()))

sorted_loc = sorted(locations, key = lambda x : x.name)

print(f'''name {sorted_loc[n-1].name}
addr {sorted_loc[n-1].num}
city {sorted_loc[n-1].loc}''')