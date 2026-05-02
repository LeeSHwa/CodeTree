array = list(map(int, input().split()))

array.sort()

A = array[0]
B = array[1]

C_plus_D = array[-1] - (A + B)

if A + B == array[2]:
    C = array[3]
else:
    C = array[2]

D = C_plus_D - C

print(A, B, C, D)
# for i in range(2, len(array) - 2):
    
#     for j in range(i + 1, len(array) - 1):

#         flag = True
#         if array[i] + array[j] == C_plus_D:
            
#             if array[i] + A not in array:
#                 flag = False
            
#             if array[j] + B not in array:
#                 flag = False

#             if array[i] + array[j] + A not in array:
#                 flag = False

#             if array[i] + array[j] + B not in array:
#                 flag = False
            
#         if flag:
#             print(A, B, array[i], array[j])
#             exit()
            