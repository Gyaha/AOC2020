def translate_row(inp: str) -> int:
    b = "0b" + (inp.replace("F", "0").replace("B", "1"))
    return int(b, 2)


def translate_column(inp: str) -> int:
    b = "0b" + (inp.replace("L", "0").replace("R", "1"))
    return int(b, 2)


def translate_pass_to_seat(inp: str) -> int:
    return (translate_row(inp[:-3]) * 8) + translate_column(inp[-3:])


def get_higest_seat(s: str) -> int:
    d = [n.strip() for n in s.splitlines()]
    h = 0
    for p in d:
        seat = translate_pass_to_seat(p)
        if seat > h:
            h = seat
    return h


def run_tests():
    test_input = "FBFBBFF"
    test_output = 44
    assert translate_row(test_input) == test_output

    test_input = "BBFFBBF"
    test_output = 102
    assert translate_row(test_input) == test_output

    test_input = "RLR"
    test_output = 5
    assert translate_column(test_input) == test_output

    test_input = "RLL"
    test_output = 4
    assert translate_column(test_input) == test_output

    test_input = "BFFFBBFRRR"
    test_output = 567
    assert translate_pass_to_seat(test_input) == test_output


def run() -> int:
    with open("inputs/input_05.txt") as file:
        data = file.read()
    return get_higest_seat(data)


if __name__ == "__main__":
    run_tests()
    print(run())
