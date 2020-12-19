def count_adapter_possibilities(s: str) -> int:
    l = sorted([0] + [int(l) for l in s.strip("\n").splitlines()])
    return recurve_adapters(l, {}, len(l) - 1)


def recurve_adapters(l: list, m: dict, i: int) -> int:
    if i in m:
        return m[i]
    if i < 1:
        return 1
    s = 0
    for g in range(1, 4):
        if i - g >= 0 and l[i] - l[i - g] <= 3:
            s += recurve_adapters(l, m, i - g)
    m[i] = s
    return s


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
    test_output = 8
    assert count_adapter_possibilities(test_input) == test_output

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
    test_output = 19208
    assert count_adapter_possibilities(test_input) == test_output


def run() -> int:
    with open("inputs/input_10.txt") as file:
        data = file.read()
    return count_adapter_possibilities(data)


if __name__ == "__main__":
    run_tests()
    print(run())
