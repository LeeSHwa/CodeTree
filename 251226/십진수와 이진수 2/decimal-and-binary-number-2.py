N = input()

# Please write your code here.

num = 0
for digit in N:
    num = num * 2 + int(digit)

num *= 17

rest = []

while True:
    if num < 2:
        rest.append(num)
        break
        
    rest.append(num%2)

    num //= 2

print(''.join(map(str, rest[::-1])))