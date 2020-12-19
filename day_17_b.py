# (x,y,z,w)
# [cube, neighbors]

from itertools import product

neighbor_offsets = [p for p in product((0, 1, -1), (0, 1, -1), (0, 1, -1), (0, 1, -1))][1:]


def set_cube(grid: dict, x: int, y: int, z: int, w: int):
    cord = (x, y, z, w)
    if not cord in grid:
        grid[cord] = [True, 0]
    else:
        grid[cord][0] = True


def add_neighbor(grid: dict, cord: tuple):
    if not cord in grid:
        grid[cord] = [False, 1]
    else:
        grid[cord][1] += 1


def calc_neighbors(grid: dict):
    t = []
    for cord, cord_values in grid.items():
        if cord_values[0]:
            t.append(cord)
    for c in t:
        for o in neighbor_offsets:
            add_neighbor(grid, (c[0] + o[0], c[1] + o[1], c[2] + o[2], c[3] + o[3]))


def calc_cubes(grid: dict):
    for v in grid.values():
        if v[0]:
            if v[1] == 2 or v[1] == 3:
                pass
            else:
                v[0] = False
        else:
            if v[1] == 3:
                v[0] = True


def calc_clean(grid: dict):
    t = []
    for c, v in grid.items():
        if not v[0]:
            t.append(c)
        else:
            v[1] = 0
    for c in t:
        grid.pop(c)


def do_turn(grid: dict):
    calc_neighbors(grid)
    calc_cubes(grid)
    calc_clean(grid)


def create_grid(s: str) -> dict:
    grid = {}
    for y, l in enumerate(s.splitlines()):
        for x, c in enumerate(list(l.strip())):
            if c == "#":
                set_cube(grid, x, y, 0, 0)
    return grid


def count_cubes(grid: dict) -> int:
    return len(grid.values())


def load_input_and_run_and_count(s: str, t: int) -> int:
    grid = create_grid(s)
    for _ in range(t):
        do_turn(grid)
    return count_cubes(grid)


def run_tests():
    test_input = """.#.
    ..#
    ###"""
    test_output = 848
    assert load_input_and_run_and_count(test_input, 6) == test_output


def run() -> int:
    with open("inputs/input_17.txt") as file:
        data = file.read()
    return load_input_and_run_and_count(data, 6)


if __name__ == "__main__":
    run_tests()
    print(run())
