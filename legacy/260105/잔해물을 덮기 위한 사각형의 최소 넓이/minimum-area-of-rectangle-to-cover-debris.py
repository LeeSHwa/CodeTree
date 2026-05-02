x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.

# 첫 번째 직사각형 넓이
first_square = (x2[0] - x1[0]) * (y2[0] - y1[0])

# i) 다 덮인 경우 
if x1[0] >= x1[1] and x2[0] <= x2[1] and y1[0] >= y1[1] and y2[0] <= y2[1]:
    print(0)

# ii) 가로만 더 큰 경우 
elif x1[0] >= x1[1] and x2[0] <= x2[1]:
    # ii-1) 덮인 도형이 위에 있을 경우
    if y2[1] >= y2[0] and y1[1] < y2[0]:
        print((x2[0] - x1[0]) * (y1[1] - y1[0]))

    # ii-2) 덮인 도형이 사이에 있을 경우
    elif y2[1] < y2[0] and y1[1] > y1[0]:
        print(first_square)

    # ii-3) 덮인 도형이 아래에 있을 경우
    else:
        print((x2[0] - x1[0]) * (y2[0] - y2[1]))
        

# iii) 세로만 더 큰 경우
elif y1[0] >= y1[1] and y2[0] <= y2[1]:
    # iii-1) 덮인 도형이 오른쪽에 있을 경우
    if x2[1] >= x2[0]:
        print((x1[1] - x1[0]) * (y2[0] - y1[0]))

    # iii-2) 덮인 도형이 사이에 있을 경우
    elif x2[1] < x2[0] and x1[1] > x1[0]:
        print(first_square)

    # iii-3) 덮인 도형이 왼쪽에 있을 경우
    else:
        print((x2[0] - x2[1]) * (y2[0] - y1[0]))
       
else:
    print(first_square)