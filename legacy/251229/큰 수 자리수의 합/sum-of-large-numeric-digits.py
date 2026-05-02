a, b, c = map(int, input().split())

# Please write your code here.
multi = a * b * c

def multi_and_sum(number):
    if number < 10:
        return number
        
    return multi_and_sum(number//10) + number % 10

print(multi_and_sum(multi))
