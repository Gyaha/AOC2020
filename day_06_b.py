def count_same_awnsers_in_group(s: str) -> int:
    l = s.strip("\n").split("\n")
    g = len(l)
    r = 0
    for n in l[0]:
        if s.count(n) == g:
            r += 1
    return r


def sum_group_awnsers(s: str) -> int:
    r = 0
    for l in s.split("\n\n"):
        r += count_same_awnsers_in_group(l)
    return r


def run_tests():
    test_input = """abcx
    abcy
    abcz"""
    test_output = 3

    assert count_same_awnsers_in_group(test_input) == test_output

    test_input = """abc

    a
    b
    c

    ab
    ac

    a
    a
    a
    a

    b"""
    test_output = 6

    assert sum_group_awnsers(test_input) == test_output


def run() -> int:
    with open("inputs/input_06.txt") as file:
        data = file.read()
    return sum_group_awnsers(data)


if __name__ == "__main__":
    run_tests()
    print(run())
