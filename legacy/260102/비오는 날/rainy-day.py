class weather:
    def __init__(self, date, day, weat):
        self.date = date
        self.day = day
        self.weat = weat


n = int(input())

weathers = []

for i in range(n):
    weathers.append(weather(*input().split()))

selection = []

for i in weathers:
    if i.weat == "Rain":
        selection.append(i)

result = sorted(selection, key = lambda x : x.date)

print(result[0].date, result[0].day, result[0].weat)