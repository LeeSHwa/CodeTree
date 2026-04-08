def is_palindrome(string):
    len_str = len(string)
    reverse = string[::-1]

    if len_str == 1:
        return True

    for i in range(len_str // 2):
        if string[i] != reverse[i]:
            return False
    
    return True
        
line = input()
result = is_palindrome(line)

if result:
    print("Yes")
else:
    print("No")