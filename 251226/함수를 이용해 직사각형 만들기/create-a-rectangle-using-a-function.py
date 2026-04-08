def print_ones(row, col):
    line = "1" * col
    for _ in range(row):
        print(line)

row, col = map(int, input().split())

print_ones(row, col)