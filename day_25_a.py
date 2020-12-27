SUBJECT = 7
DIV_THINGY = 20201227


def find_encryption_key(s: str) -> int:
    card, door = s.strip("\n").split("\n")
    card, door = int(card), int(door)

    v = 1
    card_loop = 0
    while v != card:
        card_loop += 1
        v *= SUBJECT
        v %= DIV_THINGY

    door_loop = card_loop
    while v != door:
        door_loop += 1
        v *= SUBJECT
        v %= DIV_THINGY

    v = 1
    for _ in range(door_loop):
        v *= card
        v %= DIV_THINGY
    return v


def run_tests():
    test_input = """5764801
17807724"""
    test_output = 14897079
    assert find_encryption_key(test_input) == test_output


def run() -> int:
    with open("inputs/input_25.txt") as file:
        data = file.read()
    return find_encryption_key(data)


if __name__ == "__main__":
    run_tests()
    import time
    time_start = time.perf_counter()
    print(run())
    time_end = time.perf_counter() - time_start
    print(f"Time: {time_end:0.4f} sec")
