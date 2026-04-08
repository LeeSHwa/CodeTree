devs = list(map(int, input().split()))

devs.sort()

one = devs[0] + devs[5]
two = devs[1] + devs[4]
three = devs[2] + devs[3]

print(max(one, two, three) - min(one, two, three))