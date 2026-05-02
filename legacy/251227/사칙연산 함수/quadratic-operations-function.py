def calculator(A, B, Oper):
    if Oper == "+":
        print(f"{A} + {B} = {A+B}")
        return

    elif Oper == "-":
        print(f"{A} - {B} = {A-B}")
        return

    elif Oper == "/":
        print(f"{A} / {B} = {A//B}")
        return
        
    elif Oper == "*":
        print(f"{A} * {B} = {A*B}")
        return
        
    else:
        print("False")
        return

a, o, c = input().split()

A = int(a)
B = int(c)

calculator(A, B, o)