def is_magic_number(n):
    str_n = str(n)
    num_list = []

    for char in str_n:
        num_list.append(int(char))

    if n % 2 == 0 and sum(num_list) % 5 == 0:
        return("Yes")
    else:
        return("No")

print(is_magic_number(int(input())))