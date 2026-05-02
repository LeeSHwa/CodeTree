array = list(input())

size = len(array)

count = 0

for i in range(size - 3):
    if array[i] == '(' and array[i+1] =='(':
        for j in range(i + 2, size - 1):
            if array[j] == ')' and array[j + 1] == ')':
                count += 1

# for i in range(size - 3):
#     if array[i] == '(':
#         for j in range(i + 1, size - 2):
#             if array[j] =='(':
#                 for k in range(j + 1, size - 1):
#                     if array[k] == ')':
#                         for l in range(k + 1, size):
#                             if array[l] == ')':
#                                 count += 1

print(count)
