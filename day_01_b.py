TARGET = 2020


def find_three_targets_and_multiply(arr):
    for i, a in enumerate(arr):
        for j, b in enumerate(arr):
            for k, c in enumerate(arr):
                if i == j or i == k or j == k:
                    continue
                if a + b + c == TARGET:
                    return a * b * c


test_input = [1721, 979, 366, 299, 675, 1456]
test_output = 241861950
assert find_three_targets_and_multiply(test_input) == test_output


f = open("inputs/input_01.txt")
d = [int(n) for n in f.readlines()]
f.close()
print(find_three_targets_and_multiply(d))
