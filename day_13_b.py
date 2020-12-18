def get_busses(s: str) -> list:
    busses = s.strip("\n").split("\n")[1].split(",")
    busses = [(int(b), i) for i, b in enumerate(busses) if not b == "x"]
    return busses


def find_bus_alignment(s: str) -> int:
    busses = get_busses(s)
    i = 0
    s = 1
    t, la = 0, 0
    while i < len(busses):
        t += s
        if does_bus_align(busses[i], t):
            if does_bus_align(busses[i], t + t - la):
                i += 1
                s = t - la
            else:
                la = t
    return la


def does_bus_align(b: tuple, t: int) -> bool:
    return (t + b[1]) % b[0] == 0


assert does_bus_align((7, 0), 1068781)
assert does_bus_align((13, 1), 1068781)
assert does_bus_align((59, 4), 1068781)

test_input = """939
7,13,x,x,59,x,31,19"""
test_output = 1068781
assert find_bus_alignment(test_input) == test_output

test_input = """0
17,x,13,19
"""
test_output = 3417
assert find_bus_alignment(test_input) == test_output

test_input = """0
67,7,59,61
"""
test_output = 754018
assert find_bus_alignment(test_input) == test_output

test_input = """0
1789,37,47,1889
"""
test_output = 1202161486
assert find_bus_alignment(test_input) == test_output

f = open("inputs/input_13.txt")
d = f.read()
f.close()
print(find_bus_alignment(d))
