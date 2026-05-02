import sys
N = int(input())

# Please write your code here.
rest = []
if N == 0:
    print(0)
    sys.exit()

while N != 1:
    rest.append(N % 2)
    
    N //= 2

rest = rest[::-1]
print('1' + ''.join(map(str, rest)))