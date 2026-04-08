def devide_even(array):
    # for num in array:    # 얘는 immutable한 num 변수를 새롭게 할당하는거라 
    #     if num % 2 == 0: # 인자로 받은 배열에는 영향을 안미침
    #         num //= 2

    for i in range(len(array)):
        if array[i] % 2 == 0:
            array[i] //= 2

N = int(input())
num_list = list(map(int, input().split()))

devide_even(num_list)

for i in num_list:
    print(i, end = " ")