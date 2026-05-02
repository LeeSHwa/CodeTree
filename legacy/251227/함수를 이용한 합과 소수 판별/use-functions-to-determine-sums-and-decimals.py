def is_even(N):
    if N < 10:
        if N % 2 == 0:
            return 1
        else:
            return 0
    
    else:
        temp = 0

        while N > 0:
            temp += N % 10
            N //= 10

        if temp % 2 == 0:
            return 1
        else:
            return 0


era = [False, False] + [True] * 99
for i in range(2, 11):
    if era[i]:
        for j in range(i*i, 101, i):
            era[j] = False
        
A, B = map(int, input().split())

count = 0

for num in range(A, B+1):
    if era[num]:
        count += is_even(num)

print(count)