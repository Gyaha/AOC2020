def adapter_chain(s: str) -> int:
    l = sorted([int(l) for l in s.strip("\n").splitlines()])
    c = 0
    a1, a2, a3 = 0, 0, 1
    for i in l:
        d = i - c
        c = i
        if d == 1:
            a1 += 1
        elif d == 2:
            a2 += 1
        elif d == 3:
            a3 += 1
    #print(a1, a2, a3)
    return a1 * a3


def run_tests():
    test_input = """16
    10
    15
    5
    1
    11
    7
    19
    6
    12
    4"""
    test_output = 7 * 5

    assert adapter_chain(test_input) == test_output

    test_input = """28
    33
    18
    42
    31
    14
    46
    20
    48
    47
    24
    23
    49
    45
    19
    38
    39
    11
    1
    32
    25
    35
    8
    17
    7
    9
    4
    2
    34
    10
    3"""
    test_output = 22 * 10

    assert adapter_chain(test_input) == test_output


def run() -> int:
    with open("inputs/input_10.txt") as file:
        data = file.read()
    return adapter_chain(data)


if __name__ == "__main__":
    run_tests()
    print(run())
