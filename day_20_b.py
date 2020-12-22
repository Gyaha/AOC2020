import math

EMPTY_CELL = ["+------+",
              "|      |",
              "|      |",
              "|  oo  |",
              "|  oo  |",
              "|      |",
              "|      |",
              "+------+"]

CELL_SIZE = 8

# Y, X, I, R, F
PICTURE_ORDER = [[0, 0, 2347, 0, 0],
                 [0, 1, 1871, 3, 0],
                 [0, 2, 2287, 0, 1],
                 [0, 3, 3709, 1, 1],
                 [0, 4, 3911, 0, 1],
                 [0, 5, 3529, 1, 0],
                 [0, 6, 1907, 1, 1],
                 [0, 7, 1319, 1, 1],
                 [0, 8, 1997, 1, 1],
                 [0, 9, 1399, 2, 1],
                 [0, 10, 1423, 2, 1],
                 [0, 11, 1747, 0, 1],
                 [1, 0, 1847, 1, 0],
                 [1, 1, 3803, 3, 0],
                 [1, 2, 3923, 0, 0],
                 [1, 3, 1361, 0, 1],
                 [1, 4, 2711, 1, 1],
                 [1, 5, 2039, 3, 1],
                 [1, 6, 1181, 1, 0],
                 [1, 7, 3361, 0, 0],
                 [1, 8, 1777, 1, 0],
                 [1, 9, 1103, 1, 0],
                 [1, 10, 3541, 1, 1],
                 [1, 11, 1601, 3, 1],
                 [2, 0, 1619, 0, 0],
                 [2, 1, 1097, 2, 1],
                 [2, 2, 1451, 0, 0],
                 [2, 3, 3089, 1, 1],
                 [2, 4, 1493, 0, 0],
                 [2, 5, 1439, 0, 1],
                 [2, 6, 3701, 0, 0],
                 [2, 7, 3917, 0, 0],
                 [2, 8, 3389, 0, 1],
                 [2, 9, 3251, 0, 1],
                 [2, 10, 3271, 0, 1],
                 [2, 11, 2503, 3, 0],
                 [3, 0, 2213, 2, 1],
                 [3, 1, 2081, 1, 1],
                 [3, 2, 2591, 0, 0],
                 [3, 3, 2957, 0, 1],
                 [3, 4, 1699, 0, 0],
                 [3, 5, 2909, 3, 0],
                 [3, 6, 2131, 3, 0],
                 [3, 7, 2273, 3, 1],
                 [3, 8, 2053, 1, 0],
                 [3, 9, 1163, 2, 1],
                 [3, 10, 3691, 0, 0],
                 [3, 11, 1289, 2, 1],
                 [4, 0, 1979, 3, 0],
                 [4, 1, 2683, 1, 0],
                 [4, 2, 1951, 3, 1],
                 [4, 3, 3517, 0, 0],
                 [4, 4, 3853, 3, 1],
                 [4, 5, 2621, 1, 1],
                 [4, 6, 1367, 3, 1],
                 [4, 7, 1697, 0, 0],
                 [4, 8, 2927, 0, 1],
                 [4, 9, 2393, 1, 0],
                 [4, 10, 1409, 2, 1],
                 [4, 11, 3767, 1, 0],
                 [5, 0, 1021, 1, 1],
                 [5, 1, 1483, 0, 0],
                 [5, 2, 2477, 3, 1],
                 [5, 3, 3623, 1, 1],
                 [5, 4, 2609, 0, 1],
                 [5, 5, 3209, 0, 0],
                 [5, 6, 2341, 2, 1],
                 [5, 7, 3467, 3, 0],
                 [5, 8, 3049, 1, 0],
                 [5, 9, 2269, 0, 0],
                 [5, 10, 1093, 2, 1],
                 [5, 11, 1823, 3, 0],
                 [6, 0, 2207, 1, 0],
                 [6, 1, 1129, 3, 0],
                 [6, 2, 1277, 1, 0],
                 [6, 3, 3137, 0, 0],
                 [6, 4, 2221, 0, 0],
                 [6, 5, 3019, 0, 0],
                 [6, 6, 2617, 2, 1],
                 [6, 7, 2029, 3, 0],
                 [6, 8, 3797, 3, 1],
                 [6, 9, 3329, 3, 0],
                 [6, 10, 3061, 0, 0],
                 [6, 11, 1733, 0, 0],
                 [7, 0, 3373, 0, 1],
                 [7, 1, 1231, 2, 1],
                 [7, 2, 2657, 0, 0],
                 [7, 3, 3673, 1, 0],
                 [7, 4, 1291, 0, 1],
                 [7, 5, 1223, 1, 0],
                 [7, 6, 2381, 0, 0],
                 [7, 7, 3083, 0, 1],
                 [7, 8, 3719, 0, 0],
                 [7, 9, 2267, 3, 1],
                 [7, 10, 2729, 2, 1],
                 [7, 11, 1889, 1, 1],
                 [8, 0, 3121, 2, 1],
                 [8, 1, 1171, 0, 1],
                 [8, 2, 2857, 0, 1],
                 [8, 3, 3347, 2, 1],
                 [8, 4, 2707, 3, 1],
                 [8, 5, 1933, 3, 0],
                 [8, 6, 2113, 1, 1],
                 [8, 7, 1427, 1, 1],
                 [8, 8, 2141, 0, 1],
                 [8, 9, 1787, 2, 1],
                 [8, 10, 1709, 1, 1],
                 [8, 11, 3449, 1, 1],
                 [9, 0, 2161, 0, 1],
                 [9, 1, 3581, 1, 1],
                 [9, 2, 2741, 1, 1],
                 [9, 3, 2027, 1, 0],
                 [9, 4, 3023, 1, 1],
                 [9, 5, 1213, 1, 0],
                 [9, 6, 1609, 3, 0],
                 [9, 7, 2557, 0, 0],
                 [9, 8, 1741, 1, 1],
                 [9, 9, 3889, 1, 1],
                 [9, 10, 2797, 1, 0],
                 [9, 11, 2467, 0, 0],
                 [10, 0, 1087, 1, 1],
                 [10, 1, 3677, 0, 1],
                 [10, 2, 2377, 3, 1],
                 [10, 3, 3407, 3, 0],
                 [10, 4, 2011, 0, 1],
                 [10, 5, 1627, 2, 1],
                 [10, 6, 2143, 1, 0],
                 [10, 7, 1667, 1, 0],
                 [10, 8, 3527, 1, 1],
                 [10, 9, 3793, 3, 0],
                 [10, 10, 2351, 2, 1],
                 [10, 11, 1597, 0, 0],
                 [11, 0, 2281, 1, 0],
                 [11, 1, 2579, 3, 0],
                 [11, 2, 3863, 2, 1],
                 [11, 3, 2339, 3, 1],
                 [11, 4, 1861, 2, 1],
                 [11, 5, 3821, 1, 0],
                 [11, 6, 3319, 0, 0],
                 [11, 7, 1549, 1, 0],
                 [11, 8, 1013, 0, 0],
                 [11, 9, 1151, 1, 1],
                 [11, 10, 2837, 2, 1],
                 [11, 11, 1811, 1, 1]]


MONSTER_SHAPE = """
..................#.
#....##....##....###
.#..#..#..#..#..#..."""


class Picture():
    def __init__(self, i: int, p: list):
        self.i = i
        self.p = p


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

    def set_picture(self, p: Picture, r: int, f: bool, y: int, x: int) -> bool:
        if c := self.get_cell(y, x):
            c.p = p
            c.r = r
            c.f = f
            return True
        else:
            return False


def draw_map(m: Map) -> list:
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
                for py in range(CELL_SIZE):
                    prt[(y * CELL_SIZE) + py].append(EMPTY_CELL[py])
    for i in range(len(prt)):
        prt[i] = "".join(prt[i])
    return prt


def print_map(mp: list):
    for l in mp:
        print("".join(map(str, l)))


def print_map_part(mp: list, y: int, x: int, h: int, w: int):

    for i in range(y, y + h):
        print("".join(map(str, mp[i][x:x + w])))


def create_picture(s: str) -> Picture:
    p = [j.strip() for j in s.strip().splitlines()]
    i = int(p.pop(0)[5:-1])
    size = len(p[0]) - 1

    p = create_rotated_pictures(p, size)
    crop_picture_edges(p)

    return Picture(i, p)


def crop_picture_edges(p: list):
    for pp in p:
        pp.pop(0)
        pp.pop(CELL_SIZE)
        for y in range(len(pp)):
            pl = list(pp[y])
            pl.pop(0)
            pl.pop(CELL_SIZE)
            pp[y] = "".join(pl)


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


def create_pictures(s: str) -> list:
    l = []
    for p in s.strip().split("\n\n"):
        l.append(create_picture(p))
    return l


def load_cells(m: Map, p: list):
    for j in PICTURE_ORDER:
        y, x, pp, r, f = j[0], j[1], get_picture(j[2], p), j[3], j[4]
        m.set_picture(pp, r, f, y, x)


def get_picture(i, p):
    for pp in p:
        if pp.i == i:
            return pp


def create_monster(s: str) -> list:
    m0 = []
    for l in s.strip("\n").strip().splitlines():
        m0.append([1 if a == "#" else 0 for a in l])
    m0f = [[a for a in reversed(b)] for b in m0]

    mh, mw = len(m0), len(m0[0])
    m1, m1f = [], []
    m2, m2f = [], []
    m3, m3f = [], []

    for y in range(mh):
        m2.append([a for a in reversed(m0[mh - y - 1])])
        m2f.append([a for a in reversed(m0f[mh - y - 1])])

    for x in range(mw):
        m1.append([])
        m1f.append([])
        m3.append([])
        m3f.append([])
        for y in range(mh):
            m1[x].append(m0[y][x])
            m1f[x].append(m0f[y][x])
            m3[x].append(m0[mh - y - 1][mw - x - 1])
            m3f[x].append(m0f[mh - y - 1][mw - x - 1])
    """
    for l, j in zip(m0, m0f):
        print("".join([str(c) for c in l] + [" : "] + [str(c) for c in j]))

    for l, j in zip(m1, m1f):
        print("".join([str(c) for c in l] + [" : "] + [str(c) for c in j]))

    for l, j in zip(m2, m2f):
        print("".join([str(c) for c in l] + [" : "] + [str(c) for c in j]))

    for l, j in zip(m3, m3f):
        print("".join([str(c) for c in l] + [" : "] + [str(c) for c in j]))
    """
    return [m0, m1, m2, m3, m0f, m1f, m2f, m3f]


def find_monsters(s: str):
    p = create_pictures(s)
    m_size = int(math.sqrt(len(p)))
    m = Map(m_size, m_size)
    load_cells(m, p)
    mp = draw_map(m)
    mp = [list(l) for l in mp]
    monster = create_monster(MONSTER_SHAPE)
    mc = check_map_for_monster(mp, monster)
    #print_map_part(mp, 5, 5, 10, 50)
    mark_monsters(mp, mc, monster)
    #print_map_part(mp, 5, 5, 10, 50)
    return count_non_monster_pixels(mp)


def count_non_monster_pixels(mp: list) -> int:
    s = 0
    for l in mp:
        s += l.count("#")
    return s


def mark_monsters(mp: list, mc: list, monster: list):
    hc, hr, hf = 0, 0, 0
    for r in range(4):
        for f in range(2):
            c = len(mc[r][f])
            if c > hc:
                hc = c
                hr = r
                hf = f

    mon = monster[hr + (4 if hf else 0)]
    mh, mw = len(mon), len(mon[0])
    for ms in mc[hr][hf]:
        for my in range(mh):
            for mx in range(mw):
                if mon[my][mx]:
                    mp[ms[0] + my][ms[1] + mx] = "X"


def check_map_for_monster(mp: list, monster: list) -> list:
    mh, mw = len(mp), len(mp[0])
    found = [[[], []] for r in range(4)]
    for y in range(mh):
        for x in range(mw):
            for r in range(4):
                for f in range(2):
                    if find_monster(mp, monster[r + (4 if f else 0)], y, x):
                        found[r][f].append([y, x])
    return found


def find_monster(mp: list, monster: list, y: int, x: int):
    mh, mw = len(monster), len(monster[0])
    for my in range(mh):
        for mx in range(mw):
            try:
                if monster[my][mx]:
                    if not mp[y + my][x + mx] == "#":
                        return False
            except:
                return False
    return True


def run_tests():
    pass


def run() -> int:
    with open("inputs/input_20.txt") as file:
        data = file.read()
    return find_monsters(data)


if __name__ == "__main__":
    run_tests()
    import time
    time_start = time.perf_counter()
    print(run())
    time_end = time.perf_counter() - time_start
    print(f"Time: {time_end:0.4f} sec")
