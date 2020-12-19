TARGET_TURN = 2020


def play_memory_game(s: str) -> int:
    d = [int(a) for a in s.split(",")]
    m = {}
    t = 0
    n = 0
    f = True
    for p in d:
        t += 1
        m[p] = t
    while t + 1 < TARGET_TURN:
        t += 1
        m, n = do_turn(m, n, t)
    return n


def do_turn(m: dict, n: int, t: int):
    if n in m:
        tmp = t - m[n]
        m[n] = t
        n = tmp
    else:
        m[n] = t
        n = 0
    return m, n


def run_tests():
    test_input = "0,3,6"
    test_output = 436
    assert play_memory_game(test_input) == test_output

    test_input = "1,3,2"
    test_output = 1
    assert play_memory_game(test_input) == test_output

    test_input = "2,1,3"
    test_output = 10
    assert play_memory_game(test_input) == test_output

    test_input = "1,2,3"
    test_output = 27
    assert play_memory_game(test_input) == test_output

    test_input = "2,3,1"
    test_output = 78
    assert play_memory_game(test_input) == test_output

    test_input = "3,2,1"
    test_output = 438
    assert play_memory_game(test_input) == test_output

    test_input = "3,1,2"
    test_output = 1836
    assert play_memory_game(test_input) == test_output


def run() -> int:
    with open("inputs/input_15.txt") as file:
        data = file.read()
    return play_memory_game(data)


if __name__ == "__main__":
    run_tests()
    print(run())
