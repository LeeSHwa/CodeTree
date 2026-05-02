N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

# Please write your code here.
MAX_POS = 100

m = float('inf')

for line_y in range(2, MAX_POS + 1, 2):
    for line_x in range(2, MAX_POS + 1, 2):
        # 4분위로 나눠

        counts = [0, 0, 0, 0]
        
        for x, y in points:
        # 1사분면
            if x > line_y and y > line_x:
                counts[0] += 1
        
        # 2사분면
            elif x < line_y and y > line_x:
                counts[1] += 1

        # 3사분면
            elif x < line_y and y < line_x:
                counts[2] += 1

        # 4사분면
            elif x > line_y and y < line_x:
                counts[3] += 1
        
        curr_count = max(counts)

        m = min(m, curr_count)
        

print(m)