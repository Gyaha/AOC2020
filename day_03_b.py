TREE = "#"


def hit_test(map_, y, x, width):
    while x >= width:
        x -= width
    return map_[y][x] == TREE


def hit_test_map(map_, vy, vx):
    height, width = len(map_), len(map_[0])
    r = 0
    for x, y in enumerate(range(0, height, vy)):
        r += hit_test(map_, y, x * vx, width)
    return r


def hit_test_multi(map_):
    return hit_test_map(map_, 1, 1) * hit_test_map(map_, 1, 3) * hit_test_map(map_, 1, 5) * hit_test_map(map_, 1, 7) * hit_test_map(map_, 2, 1)


test_input = ["..##.......",
              "#...#...#..",
              ".#....#..#.",
              "..#.#...#.#",
              ".#...##..#.",
              "..#.##.....",
              ".#.#.#....#",
              ".#........#",
              "#.##...#...",
              "#...##....#",
              ".#..#...#.#"]
test_output = 336

assert hit_test_map(test_input, 1, 1) == 2
assert hit_test_map(test_input, 1, 3) == 7
assert hit_test_map(test_input, 1, 5) == 3
assert hit_test_map(test_input, 1, 7) == 4
assert hit_test_map(test_input, 2, 1) == 2
assert hit_test_multi(test_input) == test_output

f = open("inputs/input_03.txt")
d = [n.replace("\n", "") for n in f.readlines()]
f.close()
print(hit_test_multi(d))
