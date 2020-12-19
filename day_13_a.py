def find_next_bus(s: str) -> int:
    target, busses = s.strip("\n").split("\n")
    target = int(target)
    busses = [int(a) if not a == "x" else None for a in busses.split(",")]
    c = []
    for bus in busses:
        if bus == None:
            continue
        w = bus - (target % bus)
        c.append([w, bus])
    next_bus = sorted(c)[0]
    return next_bus[0] * next_bus[1]


def run_tests():
    test_input = """939
    7,13,x,x,59,x,31,19"""
    test_output = 295

    assert find_next_bus(test_input) == test_output


def run() -> int:
    with open("inputs/input_13.txt") as file:
        data = file.read()
    return find_next_bus(data)


if __name__ == "__main__":
    run_tests()
    print(run())
