N, B = map(int, input().split())

# Please write your code here.

digits = []

while True:
    if N < B:
        digits.append(N)
        break
    
    digits.append(N % B)

    N //= B

digits = digits[::-1]
print(''.join(map(str, digits)))