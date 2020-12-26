TURNS = 10000000
CUPS = 1000000


def create_cups(s: str) -> int:
    cups = {}
    starting_cups = [int(l) for l in s]
    first_cup = starting_cups[0]
    latest_cup = first_cup

    for i in range(1, len(starting_cups)):
        next_cup = starting_cups[i]
        cups[latest_cup], latest_cup = next_cup, next_cup

    for i in range(max(starting_cups) + 1, CUPS + 1):
        cups[latest_cup], latest_cup = i, i

    cups[latest_cup] = first_cup

    return cups, first_cup


def play_crab_cups(s: str, t: int):
    cups, current_cup = create_cups(s)

    for _ in range(t):
        held_1 = cups[current_cup]
        held_2 = cups[held_1]
        held_3 = cups[held_2]
        held = [held_1, held_2, held_3]

        cups[current_cup] = cups[held_3]

        target_cup = current_cup - 1
        if target_cup < 1:
            target_cup = CUPS
        while target_cup in held:
            target_cup -= 1
            if target_cup < 1:
                target_cup = CUPS

        cup_next = cups[target_cup]
        cups[target_cup] = held_1
        cups[held_3] = cup_next

        current_cup = cups[current_cup]

    first_star_cup = cups[1]
    second_star_cup = cups[first_star_cup]
    return first_star_cup * second_star_cup


def run_tests():
    test_input = """389125467"""
    test_output = 149245887792
    assert play_crab_cups(test_input, TURNS) == test_output


def run() -> int:
    with open("inputs/input_23.txt") as file:
        data = file.read()
    return play_crab_cups(data, TURNS)


if __name__ == "__main__":
    run_tests()
    import time
    time_start = time.perf_counter()
    print(run())
    time_end = time.perf_counter() - time_start
    print(f"Time: {time_end:0.4f} sec")
