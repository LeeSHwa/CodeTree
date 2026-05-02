a = list(map(int, input()))

if 0 not in a:
    a[-1] = 0
else:
    for i in range(len(a)):
        if a[i] == 0:
            a[i] = 1
            break

ans = a[0]

for i in range(len(a) - 1):
    ans = ans * 2 + a[i+1]

print(ans)