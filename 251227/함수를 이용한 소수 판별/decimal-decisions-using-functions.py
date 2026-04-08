import math

def is_prime(N):
    sqrt_N = math.sqrt(N)

    for i in range(2, int(sqrt_N + 1)):
        if N % i == 0:
            return False

    return True

A, B = map(int, input().split())
prime_num_list = []

for i in range(A, B + 1):
    if is_prime(i):
        prime_num_list.append(i)

print(sum(prime_num_list))