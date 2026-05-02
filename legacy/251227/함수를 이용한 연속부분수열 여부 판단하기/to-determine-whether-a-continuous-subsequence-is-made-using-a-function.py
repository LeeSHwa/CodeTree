def is_contain(A, B):

    for i in range(len(A) - len(B) + 1):
        if(A[i:i+len(B)] == B):
            return True
    
len_A, len_B = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if is_contain(A, B):
    print("Yes")
else:
    print("No")
