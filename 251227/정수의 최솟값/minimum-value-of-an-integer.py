def find_min_value(*integer):
    return min(integer)

a, b, c = map(int, input().split())
print(find_min_value(a, b, c))