TARGET_TURN = 30000000


def play_memory_game(s: str) -> int:
    d = [int(a) for a in s.split(",")]
    m = [0] * TARGET_TURN
    for t, n in enumerate(d, 1):
        m[n] = t
    n = 0
    c = 0
    for t in range(len(d) + 1, TARGET_TURN):
        c = m[n]
        if c:
            m[n], n = t, t - c
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
