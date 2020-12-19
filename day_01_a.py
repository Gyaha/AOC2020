TARGET = 2020


def find_two_that_add_up_to_target(s: str) -> int:
    n = [int(n) for n in s.strip("\n").splitlines()]
    for i in range(len(n)):
        for j in range(i, len(n)):
            if n[i] + n[j] == TARGET:
                return n[i] * n[j]


def run() -> int:
    with open("inputs/input_01.txt") as file:
        data = file.read()
    return find_two_that_add_up_to_target(data)


def run_tests():
    test_input = """1721
    979
    366
    299
    675
    1456"""
    test_output = 514579
    assert find_two_that_add_up_to_target(test_input) == test_output


if __name__ == "__main__":
    run_tests()
    print(run())
