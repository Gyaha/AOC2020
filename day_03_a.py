TREE = "#"


def hit_test(map_, y, x, width):
    while x >= width:
        x -= width
    return map_[y][x] == TREE


def convert_to_map(s: str) -> list:
    return [n.strip() for n in s.strip("\n").splitlines()]


def hit_test_map(s: str, vy: int, vx: int) -> int:
    map_ = convert_to_map(s)
    height, width = len(map_), len(map_[0])
    r = 0
    for i in range(height):
        r += hit_test(map_, i * vy, i * vx, width)
    return r


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
    test_output = 7
    assert hit_test_map(test_input, 1, 3) == test_output


def run() -> int:
    with open("inputs/input_03.txt") as file:
        data = file.read()
    return hit_test_map(data, 1, 3)


if __name__ == "__main__":
    run_tests()
    print(run())
