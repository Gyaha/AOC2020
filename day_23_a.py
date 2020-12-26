TURNS = 100


def shift_left(l, removed, start, target):
    len_l = len(l)
    if start < target:
        for x in range(start, target - 2):
            from_index = x + 3
            to_index = x

            if to_index >= len_l:
                to_index -= len_l
            if from_index >= len_l:
                from_index -= len_l

            l[to_index] = l[from_index]

    else:
        for x in range(start, len_l + target - 2):
            from_index = x + 3
            to_index = x

            if to_index >= len_l:
                to_index -= len_l
            if from_index >= len_l:
                from_index -= len_l

            l[to_index] = l[from_index]

    st = target - 2
    for x in range(3):
        to_index = st + x
        if to_index >= len_l:
            to_index -= len_l
        l[to_index] = removed[x]


def shift_right(l, removed, start, target):
    len_l = len(l)
    if start < target:
        for x in range(start + len_l - 1, target, -1):
            from_index = x
            to_index = x + 3

            if to_index >= len_l:
                to_index -= len_l
            if from_index >= len_l:
                from_index -= len_l

            l[to_index] = l[from_index]

    else:
        for x in range(start - 1, target, -1):
            from_index = x
            to_index = x + 3

            if to_index >= len_l:
                to_index -= len_l
            if from_index >= len_l:
                from_index -= len_l

            l[to_index] = l[from_index]

    st = target + 1
    for x in range(3):
        to_index = st + x
        if to_index >= len_l:
            to_index -= len_l
        l[to_index] = removed[x]


def move_cups(l, removed, start, target):
    len_l = len(l)
    dist_left, dist_right = (len_l - target + start, target - start) if start < target else (start - target, len_l - start + target)

    if dist_left > dist_right:
        shift_left(l, removed, start, target)
    else:
        shift_right(l, removed, start, target)


def play_crab_cups(s: str, t: int):
    cups = [int(l) for l in s]
    cup_min, cup_max = min(cups), max(cups)
    len_cups = len(cups)
    current_index = 0
    current_cup = cups[current_index]
    for _ in range(t):
        removed = cups[current_index + 1:current_index + 4]
        if len_cups < current_index + 4:
            removed += cups[:(current_index + 4) - len_cups]

        target_cup = current_cup - 1
        if target_cup < cup_min:
            target_cup = cup_max
        while target_cup in removed:
            target_cup -= 1
            if target_cup < cup_min:
                target_cup = cup_max

        target_index = cups.index(target_cup)

        move_cups(cups, removed, current_index + 1, target_index)

        current_index = cups.index(current_cup) + 1
        if current_index >= len(cups):
            current_index = 0

        current_cup = cups[current_index]

    current_index = cups.index(1)
    r = []
    while len(cups) > 1:
        if current_index >= len(cups) - 1:
            r.append(cups.pop(0))
        else:
            r.append(cups.pop(current_index + 1))

    return int("".join(map(str, r)))


def run_tests():
    test_input = """389125467"""
    test_output = 92658374
    assert play_crab_cups(test_input, 10) == test_output
    test_output = 67384529
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
