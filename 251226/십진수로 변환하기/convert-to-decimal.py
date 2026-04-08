binary = input()

# Please write your code here.

num = 0

for bit in binary:

    num = num * 2 + int(bit)

print(num)