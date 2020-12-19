def validate_password(inp: str):
    rule, phrase = inp.split(": ")
    counts, target = rule.split(" ")
    min_, max_ = counts.split("-")
    count = phrase.count(target)
    return count >= int(min_) and count <= int(max_)


def count_valid_passwords(s: str) -> int:
    d = [a.strip() for a in s.strip("\n").splitlines()]
    s = 0
    for p in d:
        s += validate_password(p)
    return s


def run_tests():
    test_input = """1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc"""
    test_output = 2
    assert count_valid_passwords(test_input) == test_output


def run() -> int:
    with open("inputs/input_02.txt") as file:
        data = file.read()
    return count_valid_passwords(data)


if __name__ == "__main__":
    run_tests()
    print(run())
