def test_preamble(l: list) -> bool:
    t = l.pop()
    for i in range(len(l) - 1):
        if t - l[i] in l[i + 1:]:
            return True
    return False


def find_preamble(s: str, p: int) -> int:
    l = [int(l) for l in s.splitlines()]
    for i in range(len(l) - p):
        if not test_preamble(l[i:i + p + 1]):
            return l[i + p]


def run_tests():
    test_input = """35
    20
    15
    25
    47
    40
    62
    55
    65
    95
    102
    117
    150
    182
    127
    219
    299
    277
    309
    576"""
    test_output = 127
    assert find_preamble(test_input, 5) == test_output


def run() -> int:
    with open("inputs/input_09.txt") as file:
        data = file.read()
    return find_preamble(data, 25)


if __name__ == "__main__":
    run_tests()
    print(run())
