a, b = map(int, input().split())
n = input()

# Please write your code here.


def encoder(value, num): # int, int / 10진수 -> num진수
    
    rest = []

    while True:
        if value < num:
            rest.append(value)
            break
        
        rest.append(value % int(num))
        value //= num

    return ''.join(map(str, rest[::-1]))

def decoder(value, num): # str, int / num진수 -> 10진수
    decimal_num = 0
    
    for digit in value:
        decimal_num = decimal_num * num + int(digit)

    return decimal_num

        
decimal_num = decoder(n, a)
answer = encoder(decimal_num, b)

print(answer)