def insert_masked_data(memory: dict, bitmask: list, t: int, b: list):
    value = None
    if t in memory:
        value = memory[t]
    else:
        value = [0] * 36
    for i, m, d in zip(range(36), bitmask, b):
        if m == "X":
            value[i] = d
        else:
            value[i] = m
    #print(str(t) + " -> " + "".join(value))
    memory[t] = value


def read_docking_data(s: str):
    d = [l.strip() for l in s.strip("\n").splitlines()]
    bitmask = None
    memory = {}
    for l in d:
        s, e = l.split(" = ")
        if s == "mask":
            bitmask = list(e)
        else:
            t = int("".join(list(s)[4:-1]))
            b = list(bin(int(e))[2:].zfill(36))
            insert_masked_data(memory, bitmask, t, b)
    s = 0
    for i in memory:
        s += int("".join(memory[i]), 2)
    return s


def run_tests():
    test_input = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
    mem[8] = 11
    mem[7] = 101
    mem[8] = 0"""
    test_output = 165
    assert read_docking_data(test_input) == test_output


def run() -> int:
    with open("inputs/input_14.txt") as file:
        data = file.read()
    return read_docking_data(data)


if __name__ == "__main__":
    run_tests()
    print(run())
