TARGET = 2020


def find_two_targets_and_multiply(arr):
    for i, a in enumerate(arr):
        for j, b in enumerate(arr):
            if i == j:
                continue
            if a + b == TARGET:
                return a * b


test_input = [1721, 979, 366, 299, 675, 1456]
test_output = 514579
assert find_two_targets_and_multiply(test_input) == test_output


f = open("inputs/input_01.txt")
d = [int(n) for n in f.readlines()]
f.close()
print(find_two_targets_and_multiply(d))
