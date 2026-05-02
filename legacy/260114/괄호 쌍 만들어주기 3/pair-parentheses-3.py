line = list(input())

count = 0
for i in range(len(line)):
    if line[i] == "(":
        for j in range(i, len(line)):
            if line[j] == ")":
                count += 1

print(count)
