def make_a_square(size):
    start = 1
    end = 9

    for i in range(size):
        for j in range(size):
            if start > end:
                start = 1
            
            print(start, end = ' ')
            start += 1

        print()

n = int(input())

make_a_square(n)