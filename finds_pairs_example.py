from finds_pairs import find_pairs

numbers = [1, 9, 5, 0, 20, -4, 12, 16, 7]
target = 12
pairs = find_pairs(numbers, target)
for p in pairs:
    print("+", p[0], p[1])
