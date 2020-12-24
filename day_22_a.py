def play_combat(s: str):
    p1, p2 = s.strip().split("\n\n")
    p1, p2 = convert_cards(p1), convert_cards(p2)
    while len(p1) > 0 and len(p2) > 0:
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        if c1 > c2:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)

    w = None
    if len(p1) > 0:
        w = p1
    else:
        w = p2
    s = 0
    for i, c in enumerate(reversed(w), 1):
        s += c * i
    return s


def convert_cards(s: str) -> list:
    c = []
    for p in s.splitlines()[1:]:
        c.append(int(p))
    return c


def run_tests():
    test_input = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""
    test_output = 306
    assert play_combat(test_input) == test_output


def run() -> int:
    with open("inputs/input_22.txt") as file:
        data = file.read()
    return play_combat(data)


if __name__ == "__main__":
    run_tests()
    import time
    time_start = time.perf_counter()
    print(run())
    time_end = time.perf_counter() - time_start
    print(f"Time: {time_end:0.4f} sec")
