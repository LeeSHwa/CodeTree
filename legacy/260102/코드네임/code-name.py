class agent:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

agents = []

for i in range(5):
    codename, score = input().split()
    score = int(score)
    
    agents.append(agent(codename, score))
    
sorted_agents = sorted(agents, key = lambda agent : agent.score)

print(sorted_agents[0].codename, sorted_agents[0].score)