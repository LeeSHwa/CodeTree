A, B, x, y = map(int, input().split())

A_to_B_direct = abs(B - A)

A_x_y_B = abs(x - A) + abs(y - B)

A_y_x_B = abs(y - A) + abs(x - B)

ans = min(A_to_B_direct, A_x_y_B, A_y_x_B)

print(ans)