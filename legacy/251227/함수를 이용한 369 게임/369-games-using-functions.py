def has_369(N):
    num_list = []

    while N > 0:
        num_list.append(N % 10)
        N //= 10

    return any(d in [3, 6, 9] for d in num_list)


def is_magic_number(N):
    if N % 3 == 0 or has_369(N):
        return True
    else:
        False

        
A, B = map(int, input().split())

count = 0
for i in range(A, B+1):
    if is_magic_number(i):
        count += 1

print(count)