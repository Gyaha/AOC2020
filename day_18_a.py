def do_math(s: str) -> str:
    l = []
    for c in s.strip("\n").replace(" ", ""):
        if c.isnumeric():
            l.append(int(c))
        else:
            l.append(c)
    return do_math_in_order(l)


def do_math_in_order(l: list) -> int:
    do_math_parenthesis(l)
    do_math_sequential(l)
    return l[0]


def do_math_parenthesis(l: list):
    i = 0
    while i < len(l):
        if l[i] == "(":
            j = i
            d = 1
            while d > 0:
                j += 1
                if l[j] == "(":
                    d += 1
                elif l[j] == ")":
                    d -= 1
            l[i] = do_math_in_order(l[i + 1: j])
            del l[i + 1:j + 1]
        i += 1


def do_math_sequential(l: list):
    while len(l) > 1:
        l[0] = eval(str(l[0]) + l[1] + str(l[2]))
        del l[1:3]


def do_math_all(s: str) -> int:
    r = 0
    for l in s.strip("\n").splitlines():
        r += do_math(l)
    return r


def run_tests():
    test_input = "1 + 2 * 3 + 4 * 5 + 6"
    test_output = 71
    assert do_math(test_input) == test_output

    test_input = "1 + (2 * 3) + (4 * (5 + 6))"
    test_output = 51
    assert do_math(test_input) == test_output

    test_input = "2 * 3 + (4 * 5)"
    test_output = 26
    assert do_math(test_input) == test_output

    test_input = "5 + (8 * 3 + 9 + 3 * 4 * 3)"
    test_output = 437
    assert do_math(test_input) == test_output

    test_input = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
    test_output = 12240
    assert do_math(test_input) == test_output

    test_input = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
    test_output = 13632
    assert do_math(test_input) == test_output


def run() -> int:
    with open("inputs/input_18.txt") as file:
        data = file.read()
    return do_math_all(data)


if __name__ == "__main__":
    run_tests()
    print(run())
