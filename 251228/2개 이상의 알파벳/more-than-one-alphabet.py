def is_combine_another_alpha(string):
    unique = set()

    for i in string:
        unique.add(i)
    
    if len(unique) > 1:
        return True
    else:
        return False

A = input()

if is_combine_another_alpha(A):
    print("Yes")
else:
    print("No")

