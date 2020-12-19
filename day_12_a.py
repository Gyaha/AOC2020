def move_direction(x, y, d, n) -> (int, int):
    if d == "E":
        x += n
    elif d == "W":
        x -= n
    elif d == "S":
        y -= n
    else:  # "N"
        y += n
    return x, y


def rotate_direction(c, w, n) -> str:
    while n > 0:
        n -= 90
        if c == "E":
            if w == "L":
                c = "N"
            else:  # "R"
                c = "S"
        elif c == "W":
            if w == "L":
                c = "S"
            else:  # "R"
                c = "N"
        elif c == "S":
            if w == "L":
                c = "E"
            else:  # "R"
                c = "W"
        else:  # "N"
            if w == "L":
                c = "W"
            else:  # "R"
                c = "E"
    return c


def manhatten_dist(x: int, y: int) -> int:
    return abs(x) + abs(y)


def stumble_about(s: str) -> (int, int):
    l = [a.strip() for a in s.splitlines()]
    x, y = 0, 0
    d = "E"
    for a in l:
        b, n = a[0], int(a[1:])
        if b == "F":
            x, y = move_direction(x, y, d, n)
        elif b == "R" or b == "L":
            d = rotate_direction(d, b, n)
        else:
            x, y = move_direction(x, y, b, n)
    return x, y


def stumble_about_manhatten(s: str) -> int:
    x, y = stumble_about(s)
    return manhatten_dist(x, y)


def run_tests():
    test_input = """F10
    N3
    F7
    R90
    F11"""
    test_output = 25
    assert stumble_about_manhatten(test_input) == test_output


def run() -> int:
    with open("inputs/input_12.txt") as file:
        data = file.read()
    return stumble_about_manhatten(data)


if __name__ == "__main__":
    run_tests()
    print(run())
