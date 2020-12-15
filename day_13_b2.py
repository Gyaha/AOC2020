def find_next_bus_restart(s: str) -> int:
    busses = s.strip("\n").split("\n")[1]
    busses = [int(a) if not a == "x" else None for a in busses.split(",")]
    b = []
    for i, bus in enumerate(busses):
        if not bus == None:
            b.append([bus, i])
    return recursively_find_tha_bus(b)


def recursively_find_tha_bus(b: list, i: int = 0, t: int = 0, p: int = 1) -> int:
    if i == len(b):
        return t
    lt = 1
    while True:
        t += p
        if check_busses_to(b, i, t):
            if check_busses_to(b, i + 1, t):
                d = t - lt
                if check_busses_to(b, i + 1, t + d):
                    return recursively_find_tha_bus(b, i + 1, lt, d)
                else:
                    lt = t


def check_busses_to(b: list, i: int, t: int) -> bool:
    for j in range(i):
        if not check_bus(b[j], t):
            return False
    return True


def check_bus(bus: list, t: int) -> bool:
    return (t + bus[1]) % bus[0] == 0


assert check_bus([7, 0], 1068781)
assert check_bus([13, 1], 1068781)
assert check_bus([59, 4], 1068781)

assert check_busses_to([[7, 0], [13, 1], [59, 4]], 3, 1068781)

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
