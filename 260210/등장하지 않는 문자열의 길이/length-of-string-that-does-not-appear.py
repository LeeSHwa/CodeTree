N = int(input())
string = input()

min_length = float('inf')

for length in range(1, N + 1):
    
    flag = True
    sett = set()
    
    for idx in range(N - length + 1):
        length_set = len(sett)

        temp = string[idx : idx + length]

        sett.add(temp)

        if length_set == len(sett):
            flag = False
            break
    
    if flag:
        min_length = min(min_length, len(temp))            

print(min_length)