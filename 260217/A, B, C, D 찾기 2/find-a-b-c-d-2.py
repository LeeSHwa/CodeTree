array = list(map(int, input().split()))

array.sort()

A = array[0]
B = array[1]

C_plus_D = array[-1] - (A + B)

D = array[-4] - (A + B) 
C = C_plus_D - D

print(A, B, C, D)