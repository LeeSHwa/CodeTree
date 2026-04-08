def swap(a, b):
    a, b = b, a
    return a, b

n, m = map(int, input().split())

ans_1, ans_2 = swap(n, m)

print(ans_1, ans_2)