TREE = "#"


def hit_test(map_, y, x, width) -> bool:
    while x >= width:
        x -= width
    return map_[y][x] == TREE


def hit_test_map(map_, vy, vx) -> int:
    height, width = len(map_), len(map_[0])
    r = 0
    for x, y in enumerate(range(0, height, vy)):
        r += hit_test(map_, y, x * vx, width)
    return r


def convert_to_map(s: str) -> list:
    return [n.strip() for n in s.strip("\n").splitlines()]


def hit_test_multi(s: str) -> int:
    map_ = convert_to_map(s)
    return hit_test_map(map_, 1, 1) * hit_test_map(map_, 1, 3) * hit_test_map(map_, 1, 5) * hit_test_map(map_, 1, 7) * hit_test_map(map_, 2, 1)


def run_tests():
    test_input = """..##.......
    #...#...#..
    .#....#..#.
    ..#.#...#.#
    .#...##..#.
    ..#.##.....
    .#.#.#....#
    .#........#
    #.##...#...
    #...##....#
    .#..#...#.#"""
    test_output = 336
    test_map = convert_to_map(test_input)

    assert hit_test_map(test_map, 1, 1) == 2
    assert hit_test_map(test_map, 1, 3) == 7
    assert hit_test_map(test_map, 1, 5) == 3
    assert hit_test_map(test_map, 1, 7) == 4
    assert hit_test_map(test_map, 2, 1) == 2
    assert hit_test_multi(test_input) == test_output


def run() -> int:
    with open("inputs/input_03.txt") as file:
        data = file.read()
    return hit_test_multi(data)


if __name__ == "__main__":
    run_tests()
    print(run())
