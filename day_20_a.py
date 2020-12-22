import math
import time

EMPTY_CELL = ["+--------+",
              "|        |",
              "|        |",
              "|        |",
              "|   oo   |",
              "|   oo   |",
              "|        |",
              "|        |",
              "|        |",
              "+--------+"]

CELL_SIZE = 10


class Picture():
    def __init__(self, i: int, p: list, n: list, e: list, s: list, w: list):
        self.i = i
        self.p = p
        self.n = n  # 0
        self.e = e  # 1
        self.s = s  # 2
        self.w = w  # 3

        self.n_r = [n for n in reversed(self.n)]
        self.e_r = [n for n in reversed(self.e)]
        self.s_r = [n for n in reversed(self.s)]
        self.w_r = [n for n in reversed(self.w)]

    def connector(self, direction: int, flipped: bool) -> list:
        if direction == 0:
            return self.n_r if flipped else self.n
        elif direction == 1:
            return self.w_r if flipped else self.e
        elif direction == 2:
            return self.s_r if flipped else self.s
        elif direction == 3:
            return self.e_r if flipped else self.w
        else:
            print(f"ERROR: direction {direction} not valid")
            return None

    def connector_r(self, direction: int, flipped: bool) -> list:
        if direction == 0:
            return self.n if flipped else self.n_r
        elif direction == 1:
            return self.w if flipped else self.e_r
        elif direction == 2:
            return self.s if flipped else self.s_r
        elif direction == 3:
            return self.e if flipped else self.w_r
        else:
            print(f"ERROR: direction {direction} not valid")
            return None


class Cell():
    def __init__(self):
        self.p = None
        self.r = 0
        self.f = False


class Map():
    def __init__(self, h: int, w: int):
        self.h = h
        self.w = w
        self.l = h * w
        self.c = [Cell() for _ in range(self.l)]

    def get_cell(self, y: int, x: int) -> Cell:
        if y < 0 or y >= self.h or x < 0 or x >= self.w:
            return None
        return self.c[(y * self.w) + x]

    def can_place_picture(self, p: Picture, r: int, f: bool, y: int, x: int) -> bool:
        c = self.get_cell(y - 1, x)  # N
        if c and c.p:
            if not can_place_picture_next_to(0, p, r, f, c.p, c.r, c.f):
                return False
        c = self.get_cell(y, x + 1)  # E
        if c and c.p:
            if not can_place_picture_next_to(1, p, r, f, c.p, c.r, c.f):
                return False
        c = self.get_cell(y + 1, x)  # S
        if c and c.p:
            if not can_place_picture_next_to(2, p, r, f, c.p, c.r, c.f):
                return False
        c = self.get_cell(y, x - 1)  # W
        if c and c.p:
            if not can_place_picture_next_to(3, p, r, f, c.p, c.r, c.f):
                return False
        return True

    def del_picture(self, y: int, x: int):
        c = self.get_cell(y, x)
        c.p = None
        c.r = 0
        c.f = False

    def set_picture(self, p: Picture, r: int, f: bool, y: int, x: int) -> bool:
        if c := self.get_cell(y, x):
            c.p = p
            c.r = r
            c.f = f
            return True
        else:
            return False

    def try_place_picture(self, p: Picture, r: int, f: bool, y: int, x: int) -> bool:
        if self.can_place_picture(p, r, f, y, x):
            return self.set_picture(p, r, f, y, x)
        else:
            return False


def print_map(m: Map):
    prt = []
    while len(prt) < m.h * CELL_SIZE:
        prt.append([])
    for y in range(m.h):
        for x in range(m.w):
            if (c := m.get_cell(y, x)) and (p := c.p):
                for py in range(CELL_SIZE):
                    rf = c.r + (4 if c.f else 0)
                    prt[(y * CELL_SIZE) + py].append(p.p[rf][py])
            else:
                # Draw empty cell
                for py in range(CELL_SIZE):
                    prt[(y * CELL_SIZE) + py].append(EMPTY_CELL[py])
                pass
    for l in prt:
        print("".join(l))


def can_connect_picture_edges(p1: Picture, d1: int, f1: bool, p2: Picture, d2: int, f2: bool) -> bool:
    return p1.connector(d1, f1) == p2.connector_r(d2, f2)


def rotate_direction(d: int, r: int) -> int:
    d += r
    if d > 3:
        d -= 4
    return d


def can_place_picture_next_to(d: int, p1: Picture, r1: int, f1: bool, p2: Picture, r2: int, f2: bool) -> bool:
    """
    d = direction(0: p2 above p1, 1: p2 right of p1, etc.)\n
    p1 / 2 = Picture1 / 2\n
    r1 / 2 = rotation(0: n=n, 1: n=e)\n
    f1 / 2 = flipped(y axis)
    """
    d1, d2 = 0, 0
    if d == 0:  # p2 above p1
        d1 = 0
        d2 = 2
    elif d == 1:  # p2 right of p1
        d1 = 1
        d2 = 3
    elif d == 2:  # p2 below p1
        d1 = 2
        d2 = 0
    elif d == 3:  # p2 left of p1
        d1 = 3
        d2 = 1
    return can_connect_picture_edges(p1, rotate_direction(d1, r1), f1, p2, rotate_direction(d2, r2), f2)


def create_picture(s: str) -> Picture:
    p = [j.strip() for j in s.strip().splitlines()]
    i = int(p.pop(0)[5:-1])
    size = len(p[0]) - 1
    n, e, s, w = [], [], [], []

    n = list(p[0])
    s = list(p[size])

    for j in p:
        w.append(j[0])
        e.append(j[size])

    # (CW)
    s.reverse()
    w.reverse()

    n = convert_edge(n)
    e = convert_edge(e)
    s = convert_edge(s)
    w = convert_edge(w)

    p = create_rotated_pictures(p, size)

    return Picture(i, p, n, e, s, w)


def create_rotated_pictures(p0: list, size: int) -> list:
    p0f = ["".join([j for j in reversed(list(l))]) for l in p0]
    p1 = [[] for _ in range(size + 1)]
    p1f = [[] for _ in range(size + 1)]
    p2 = []
    p2f = []
    p3 = [[] for _ in range(size + 1)]
    p3f = [[] for _ in range(size + 1)]

    for y in range(size + 1):
        p2.append("".join([s for s in reversed(p0[size - y])]))
        p2f.append("".join([s for s in reversed(p0f[size - y])]))
        for x in range(size + 1):
            p1[y].append(p0[x][size - y])
            p1f[y].append(p0f[x][size - y])
            p3[y].append(p0[size - x][y])
            p3f[y].append(p0f[size - x][y])
        p1[y] = "".join(p1[y])
        p1f[y] = "".join(p1f[y])
        p3[y] = "".join(p3[y])
        p3f[y] = "".join(p3f[y])
    """
    mark_picture(p0, 4, 4, "0")
    mark_picture(p0f, 4, 4, "0f")
    mark_picture(p1, 4, 4, "1")
    mark_picture(p1f, 4, 4, "1f")
    mark_picture(p2, 4, 4, "2")
    mark_picture(p2f, 4, 4, "2f")
    mark_picture(p3, 4, 4, "3")
    mark_picture(p3f, 4, 4, "3f")
    """
    """
    print("0")
    for l, lf in zip(p0, p0f):
        print(l + " > " + lf)
    print("1")
    for l, lf in zip(p1, p1f):
        print(l + " > " + lf)
    print("2")
    for l, lf in zip(p2, p2f):
        print(l + " > " + lf)
    print("3")
    for l, lf in zip(p3, p3f):
        print(l + " > " + lf)
    """
    return [p0, p1, p2, p3, p0f, p1f, p2f, p3f]


def mark_picture(l: list, y: int, x: int, s: str) -> list:
    s = list(s)
    pl = list(l[y])
    for c in range(len(s)):
        pl[x + c] = s[c]
    l[y] = "".join(pl)


def convert_edge(l: list) -> list:
    return [1 if i == "#" else 0 for i in l]


def create_pictures(s: str) -> list:
    l = []
    for p in s.strip().split("\n\n"):
        l.append(create_picture(p))
    return l


def smash_pictures_into_map(m: Map, n: int, p: list, u: list):
    if n >= m.l:
        return True
    y, x = n // m.w, n % m.w
    for i in range(len(p)):
        if i in u:
            continue
        u.append(i)
        for r in range(4):
            for f in range(2):
                if m.try_place_picture(p[i], r, f, y, x):
                    # print()
                    # print_map(m)
                    # time.sleep(1)
                    if smash_pictures_into_map(m, n + 1, p, u):
                        return True
                m.del_picture(y, x)
        u.remove(i)


def find_corner_tiles(s: str):
    p = create_pictures(s)
    m_size = int(math.sqrt(len(p)))
    m = Map(m_size, m_size)
    if smash_pictures_into_map(m, 0, p, []):
        p1 = m.get_cell(0, 0).p.i
        p2 = m.get_cell(0, m.w - 1).p.i
        p3 = m.get_cell(m.h - 1, 0).p.i
        p4 = m.get_cell(m.h - 1, m.w - 1).p.i
        return p1 * p2 * p3 * p4


def run_tests():
    test_input_1 = """Tile 2311:
    ..##.#..#.
    ##..#.....
    #...##..#.
    ####.#...#
    ##.##.###.
    ##...#.###
    .#.#.#..##
    ..#....#..
    ###...#.#.
    ..###..###"""

    test_picture_1 = create_picture(test_input_1)

    test_n = [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]
    test_e = [0, 0, 0, 1, 0, 1, 1, 0, 0, 1]
    test_s = [1, 1, 1, 0, 0, 1, 1, 1, 0, 0]  # (CW)
    test_w = [0, 1, 0, 0, 1, 1, 1, 1, 1, 0]  # (CW)
    test_n_r = [0, 1, 0, 0, 1, 0, 1, 1, 0, 0]
    test_e_r = [1, 0, 0, 1, 1, 0, 1, 0, 0, 0]
    test_s_r = [0, 0, 1, 1, 1, 0, 0, 1, 1, 1]
    test_w_r = [0, 1, 1, 1, 1, 1, 0, 0, 1, 0]

    assert test_picture_1.n == test_n
    assert test_picture_1.e == test_e
    assert test_picture_1.s == test_s
    assert test_picture_1.w == test_w
    assert test_picture_1.n_r == test_n_r
    assert test_picture_1.e_r == test_e_r
    assert test_picture_1.s_r == test_s_r
    assert test_picture_1.w_r == test_w_r

    assert test_picture_1.connector(0, False) == test_n
    assert test_picture_1.connector(0, True) == test_n_r
    assert test_picture_1.connector(1, False) == test_e
    assert test_picture_1.connector(1, True) == test_w_r
    assert test_picture_1.connector(2, False) == test_s
    assert test_picture_1.connector(2, True) == test_s_r
    assert test_picture_1.connector(3, False) == test_w
    assert test_picture_1.connector(3, True) == test_e_r

    assert can_connect_picture_edges(test_picture_1, 0, False, test_picture_1, 0, True) == True
    assert can_connect_picture_edges(test_picture_1, 0, False, test_picture_1, 0, False) == False
    assert can_connect_picture_edges(test_picture_1, 0, True, test_picture_1, 0, True) == False

    assert can_connect_picture_edges(test_picture_1, 1, False, test_picture_1, 3, True) == True
    assert can_connect_picture_edges(test_picture_1, 3, True, test_picture_1, 1, False) == True
    assert can_connect_picture_edges(test_picture_1, 1, True, test_picture_1, 1, True) == False
    assert can_connect_picture_edges(test_picture_1, 1, False, test_picture_1, 3, False) == False

    assert can_place_picture_next_to(0, test_picture_1, 0, False, test_picture_1, 2, True) == True
    assert can_place_picture_next_to(0, test_picture_1, 0, True, test_picture_1, 2, False) == True
    assert can_place_picture_next_to(0, test_picture_1, 0, False, test_picture_1, 2, False) == False

    assert can_place_picture_next_to(1, test_picture_1, 0, False, test_picture_1, 0, True) == True
    assert can_place_picture_next_to(1, test_picture_1, 0, False, test_picture_1, 1, True) == False

    assert can_place_picture_next_to(2, test_picture_1, 0, False, test_picture_1, 2, True) == True
    assert can_place_picture_next_to(3, test_picture_1, 0, False, test_picture_1, 0, True) == True

    assert can_place_picture_next_to(0, test_picture_1, 2, False, test_picture_1, 0, True) == True
    assert can_place_picture_next_to(0, test_picture_1, 3, False, test_picture_1, 3, True) == True
    assert can_place_picture_next_to(0, test_picture_1, 3, False, test_picture_1, 3, False) == False

    test_map = Map(3, 3)
    assert test_map.can_place_picture(test_picture_1, 0, True, 0, 0) == True
    assert test_map.try_place_picture(test_picture_1, 0, False, 0, 0) == True
    assert test_map.try_place_picture(test_picture_1, 2, True, 1, 0) == True
    assert test_map.try_place_picture(test_picture_1, 2, False, 1, 1) == True
    assert test_map.try_place_picture(test_picture_1, 2, False, 0, 1) == False

    test_input = """Tile 2311:
    ..##.#..#.
    ##..#.....
    #...##..#.
    ####.#...#
    ##.##.###.
    ##...#.###
    .#.#.#..##
    ..#....#..
    ###...#.#.
    ..###..###

    Tile 1951:
    #.##...##.
    #.####...#
    .....#..##
    #...######
    .##.#....#
    .###.#####
    ###.##.##.
    .###....#.
    ..#.#..#.#
    #...##.#..

    Tile 1171:
    ####...##.
    #..##.#..#
    ##.#..#.#.
    .###.####.
    ..###.####
    .##....##.
    .#...####.
    #.##.####.
    ####..#...
    .....##...

    Tile 1427:
    ###.##.#..
    .#..#.##..
    .#.##.#..#
    #.#.#.##.#
    ....#...##
    ...##..##.
    ...#.#####
    .#.####.#.
    ..#..###.#
    ..##.#..#.

    Tile 1489:
    ##.#.#....
    ..##...#..
    .##..##...
    ..#...#...
    #####...#.
    #..#.#.#.#
    ...#.#.#..
    ##.#...##.
    ..##.##.##
    ###.##.#..

    Tile 2473:
    #....####.
    #..#.##...
    #.##..#...
    ######.#.#
    .#...#.#.#
    .#########
    .###.#..#.
    ########.#
    ##...##.#.
    ..###.#.#.

    Tile 2971:
    ..#.#....#
    #...###...
    #.#.###...
    ##.##..#..
    .#####..##
    .#..####.#
    #..#.#..#.
    ..####.###
    ..#.#.###.
    ...#.#.#.#

    Tile 2729:
    ...#.#.#.#
    ####.#....
    ..#.#.....
    ....#..#.#
    .##..##.#.
    .#.####...
    ####.#.#..
    ##.####...
    ##..#.##..
    #.##...##.

    Tile 3079:
    #.#.#####.
    .#..######
    ..#.......
    ######....
    ####.#..#.
    .#...#.##.
    #.#####.##
    ..#.###...
    ..#.......
    ..#.###..."""
    test_output = 20899048083289
    assert find_corner_tiles(test_input) == test_output


def run() -> int:
    with open("inputs/input_20.txt") as file:
        data = file.read()
    return find_corner_tiles(data)


if __name__ == "__main__":
    run_tests()
    import time
    time_start = time.perf_counter()
    print(run())
    time_end = time.perf_counter() - time_start
    print(f"Time: {time_end:0.4f} sec")
