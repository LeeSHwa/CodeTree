def is_real(Month, Day):
        
    #                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
    num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # day_of_the_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    if 0 < Month < 13 and 0 < Day < 32:
        if Day > num_of_days[Month]:
            return False
        return True
    else:
        return False
    
M, D = map(int, input().split())

if is_real(M, D):
    print("Yes")
else:
    print("No")


