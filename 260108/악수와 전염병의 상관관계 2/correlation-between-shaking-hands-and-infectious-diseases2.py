class log:
    def __init__(self, sec, x, y):
        self.sec = sec
        self.x = x
        self.y = y

class dev:
    def __init__(self, is_infected, k):
        self.is_infected = is_infected
        self.k = k

N, K, P, T = map(int, input().split())

devs = [0]
for i in range(1, N+1):
    if i == P:
        devs.append(dev(1, K))
    else:
        devs.append(dev(0, 0))

logs = []

for _ in range(T):
    t, x, y = map(int, input().split())
    logs.append(log(t, x, y))

logs.sort(key = lambda x : x.sec)

for hand in logs:
    if devs[hand.x].is_infected == 0 and devs[hand.y].is_infected == 0:
        continue

    elif devs[hand.x].is_infected and devs[hand.y].is_infected:
        if devs[hand.x].k > 0:
            devs[hand.x].k -= 1
        if devs[hand.y].k > 0:
            devs[hand.y].k -= 1

    elif devs[hand.x].is_infected and devs[hand.y].is_infected == 0:
        if devs[hand.x].k > 0:
            devs[hand.x].k -= 1
            devs[hand.y].is_infected = 1
            devs[hand.y].k = K
        else:
            continue

    elif devs[hand.y].is_infected and devs[hand.x].is_infected == 0:
        if devs[hand.y].k > 0:
            devs[hand.y].k -= 1
            devs[hand.x].is_infected = 1
            devs[hand.x].k = K
        else:
            continue

for i in range(1, N+1):
    print(devs[i].is_infected, end="")