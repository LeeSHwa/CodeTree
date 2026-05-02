N = int(input())
numbers = list(map(int, input().split()))

odd = 0
even = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

while even < odd:
    odd -= 2
    even += 1


while even > odd + 1:
    even -= 1

print(odd + even)