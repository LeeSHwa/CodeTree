MAX_X = 10

N = int(input())

points = [tuple(map(int, input().split())) for _ in range(N)]

cnt = 0
for i in range(MAX_X + 1):
    for j in range(MAX_X + 1):
        for k in range(MAX_X + 1):

            flag = True
            
            for x, _ in points:
                if x == i or x == j or x == k:
                    continue 

                flag = False

            if flag:
                cnt = 1

            flag = True

            for x, y in points:    
                if x == i or x == j or y == k:
                    continue 

                flag = False

            if flag:
                cnt = 1

            flag = True

            for x, y in points:
                if x == i or y == j or y == k:
                    continue 

                flag = False

            if flag:
                cnt = 1

            flag = True

            for _, y in points:
                if y == i or y == j or y == k:
                    continue

                flag = False
        
            if flag:
                cnt = 1

print(cnt)