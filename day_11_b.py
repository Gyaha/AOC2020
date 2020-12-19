import copy


def print_map(seat_map):
    for l in seat_map:
        print("".join(l))
    print("")


def look_direction(seat_map: list, h: int, w: int, x: int, y: int, vx: int, vy: int) -> str:
    t = get_tile(seat_map, h, w, x + vx, y + vy)
    if t == ".":
        return look_direction(seat_map, h, w, x + vx, y + vy, vx, vy)
    return t


def count_seated_around(seat_map: list, h: int, w: int, x: int, y: int) -> int:
    c = 0
    c += look_direction(seat_map, h, w, x, y, -1, -1) == "#"
    c += look_direction(seat_map, h, w, x, y, 0, -1) == "#"
    c += look_direction(seat_map, h, w, x, y, +1, -1) == "#"

    c += look_direction(seat_map, h, w, x, y, -1, 0) == "#"
    c += look_direction(seat_map, h, w, x, y, +1, 0) == "#"

    c += look_direction(seat_map, h, w, x, y, -1, +1) == "#"
    c += look_direction(seat_map, h, w, x, y, 0, +1) == "#"
    c += look_direction(seat_map, h, w, x, y, +1, +1) == "#"

    return c


def get_tile(seat_map: list, h: int, w: int, x: int, y: int) -> str:
    if x < 0 or x >= w or y < 0 or y >= h:
        return None
    return seat_map[y][x]


def set_tile(seat_map: list, h: int, w: int, x: int, y: int, n: str):
    if x < 0 or x >= w or y < 0 or y >= h:
        return
    seat_map[y][x] = n


def simulate_seats(seat_map: list) -> bool:
    h, w = len(seat_map), len(seat_map[0])
    seat_map_old = copy.deepcopy(seat_map)
    dirty = False
    for y in range(h):
        for x in range(w):
            t = get_tile(seat_map_old, h, w, x, y)
            if t == "L":
                c = count_seated_around(seat_map_old, h, w, x, y)
                if c == 0:
                    set_tile(seat_map, h, w, x, y, "#")
                    dirty = True
            elif t == "#":
                c = count_seated_around(seat_map_old, h, w, x, y)
                if c >= 5:
                    set_tile(seat_map, h, w, x, y, "L")
                    dirty = True
    return dirty


def simulate_seatmap(s: str) -> int:
    seat_map = [[b for b in a.strip()] for a in s.splitlines()]
    while simulate_seats(seat_map):
        pass
    c = 0
    for l in seat_map:
        c += l.count("#")
    return c


def run_tests():
    test_input = """L.LL.LL.LL
    LLLLLLL.LL
    L.L.L..L..
    LLLL.LL.LL
    L.LL.LL.LL
    L.LLLLL.LL
    ..L.L.....
    LLLLLLLLLL
    L.LLLLLL.L
    L.LLLLL.LL"""
    test_output = 26
    assert simulate_seatmap(test_input) == test_output


def run() -> int:
    with open("inputs/input_11.txt") as file:
        data = file.read()
    return simulate_seatmap(data)


if __name__ == "__main__":
    run_tests()
    print(run())
