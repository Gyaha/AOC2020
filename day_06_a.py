def count_unique_awnsers_in_group(s: str) -> int:
    return len(set(list(s.replace("\n", "").replace(" ", ""))))


def sum_group_awnsers(s: str) -> int:
    r = 0
    for l in s.split("\n\n"):
        r += count_unique_awnsers_in_group(l)
    return r


def run_tests():
    test_input = """abcx
    abcy
    abcz"""
    test_output = 6

    assert count_unique_awnsers_in_group(test_input) == test_output

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
    test_output = 11

    assert sum_group_awnsers(test_input) == test_output


def run() -> int:
    with open("inputs/input_06.txt") as file:
        data = file.read()
    return sum_group_awnsers(data)


if __name__ == "__main__":
    run_tests()
    print(run())
