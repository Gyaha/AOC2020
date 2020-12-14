from functools import reduce

# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
# (This is black magic)


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def find_next_bus_restart(s: str) -> int:
    busses = s.strip("\n").split("\n")[1]
    busses = [int(a) if not a == "x" else None for a in busses.split(",")]
    b = []
    for i, bus in enumerate(busses):
        if not bus == None:
            b.append([bus, -i])
    n, a = [], []
    for j in sorted(b):
        n.append(j[0])
        a.append(j[1])
    return chinese_remainder(n, a)


def is_prime(i: int) -> bool:
    if i == None:
        return True
    if i <= 1:
        return False
    for j in range(2, i):
        if (j % i) == 0:
            return False
    return True


assert chinese_remainder([27, 20], [15, 16]) == 96
assert chinese_remainder([3, 5, 7], [2, 3, 2]) == 23
assert chinese_remainder([7, 13, 19, 31, 59], [0, -1, -7, -6, -4]) == 1068781


test_input = """939
7,13,x,x,59,x,31,19"""
test_output = 1068781
assert find_next_bus_restart(test_input) == test_output

test_input = """0
17,x,13,19
"""
test_output = 3417
assert find_next_bus_restart(test_input) == test_output

test_input = """0
67,7,59,61
"""
test_output = 754018
assert find_next_bus_restart(test_input) == test_output

test_input = """0
1789,37,47,1889
"""
test_output = 1202161486
assert find_next_bus_restart(test_input) == test_output

f = open("inputs/input_13.txt")
d = f.read()
f.close()
print(find_next_bus_restart(d))
