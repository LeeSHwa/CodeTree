def is_leapYear(y):
    if y % 100 == 0 and y % 400 != 0:
        return False
        
    if y % 4 == 0:
        return True
    else:
        return False

y = int(input())

if is_leapYear(y):
    print("true")
else:
    print("false")