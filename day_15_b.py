TARGET_TURN = 30000000 - 1


def play_memory_game(s: str) -> int:
    d = [int(a) for a in s.split(",")]
    m = [None] * 30000000
    t = 0
    n = 0
    for p in d:
        t += 1
        m[p] = t
    while t < TARGET_TURN:
        t += 1
        if m[n]:
            m[n], n = t, t - m[n]
        else:
            m[n], n = t, 0
    return n


def run_tests():
    test_input = "0,3,6"
    test_output = 175594
    assert play_memory_game(test_input) == test_output


def run() -> int:
    with open("inputs/input_15.txt") as file:
        data = file.read()
    return play_memory_game(data)


if __name__ == "__main__":
    run_tests()
    print(run())
