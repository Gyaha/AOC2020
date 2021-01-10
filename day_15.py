import day_15_wrapper as _c


def play_memory_game(s: str, to_turn: int) -> int:
    starting_turns = [int(x) for x in s.splitlines()[0].split(",")]

    starting_memory = [0]
    for i, n in enumerate(starting_turns, 1):
        while len(starting_memory) <= n:
            starting_memory.append(0)
        starting_memory[n] = i

    starting_turn = len(starting_turns)

    _c.start_game(starting_memory, starting_turn, to_turn)
    return _c.play_to_turn(to_turn)


def run_tests():
    test_input = "0,3,6"
    test_output = 436

    assert play_memory_game(test_input, 2020) == test_output

    test_input = "2,3,1"
    test_output = 6895259

    assert play_memory_game(test_input, 30000000) == test_output


def run_a() -> int:
    with open("inputs/input_15.txt") as file:
        data = file.read()
    return play_memory_game(data, 2020)


def run_b() -> int:
    with open("inputs/input_15.txt") as file:
        data = file.read()
    return play_memory_game(data, 30000000)


if __name__ == "__main__":
    run_tests()
    print(run_a())
    print(run_b())
