TREE = "#"


def hit_test(map_, y, x, width):
    while x >= width:
        x -= width
    return map_[y][x] == TREE


def hit_test_map(map_):
    height, width = len(map_), len(map_[0])
    r = 0
    for y in range(height):
        r += hit_test(map_, y, y * 3, width)
    return r


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
test_output = 7

assert hit_test_map(test_input) == test_output

f = open("inputs/input_03.txt")
d = [n.replace("\n", "") for n in f.readlines()]
f.close()
print(hit_test_map(d))
