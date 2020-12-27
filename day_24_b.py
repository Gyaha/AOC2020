def print_tiles(tiles, s, n: bool = False):
    size = (s * 2) + 1
    offset = s + 1
    l = [["." for _ in range(size)] for _ in range(size)]
    for y in range(size):
        for x in range(size):
            tile = (y - offset, x - offset)
            if tile in tiles:
                tile = tiles[tile]
                if tile[0]:
                    if tile[1] == 0 or tile[1] > 2:
                        l[y][x] = "X"
                    else:
                        l[y][x] = "#"
                else:
                    l[y][x] = str(tile[1])

    for i, y in enumerate(l):
        print("" if not i % 2 == 0 else " ", " ".join(y))


def flip_tiles(s: str) -> dict:
    tiles = {}
    y, x = 0, 0
    turns = [list(a) for a in s.strip().splitlines()]
    for turn in turns:
        i = 0
        y, x = 0, 0
        while i < len(turn):
            r = False
            t = turn[i]
            if t == "w":
                x -= 1
            elif t == "e":
                x += 1
            elif t == "n":
                y += 1
                r = True
            elif t == "s":
                y -= 1
                r = True

            if r:
                i += 1
                t = turn[i]
                if y % 2 == 0:
                    x += 1
                if t == "w":
                    x -= 1
            i += 1
        tile = (y, x)
        if tile in tiles.keys():
            tiles.pop(tile)
        else:
            tiles[tile] = [True, 0]

    return tiles


def add_neighbor(tiles, y, x):
    tile = (y, x)
    if not tile in tiles.keys():
        tiles[tile] = [False, 1]
    else:
        tiles[tile][1] += 1


def add_neighbors(tiles, y, x):
    add_neighbor(tiles, y, x - 1)
    add_neighbor(tiles, y, x + 1)
    if not y % 2 == 0:
        x += 1
    add_neighbor(tiles, y + 1, x)
    add_neighbor(tiles, y + 1, x - 1)
    add_neighbor(tiles, y - 1, x)
    add_neighbor(tiles, y - 1, x - 1)


def play_game_of_life(s: str, t: int) -> int:
    tiles = flip_tiles(s)

    for _ in range(t):
        for tile in list(tiles.keys()):
            add_neighbors(tiles, tile[0], tile[1])

        #print_tiles(tiles, 20, True)
        # input()

        rem = []
        for t in tiles.keys():
            tile = tiles[t]
            if tile[0]:
                if tile[1] == 0 or tile[1] > 2:
                    tile[0] = False
                    rem.append(t)
                else:
                    tile[1] = 0
            else:
                if tile[1] == 2:
                    tile[0] = True
                    tile[1] = 0
                else:
                    rem.append(t)

        for r in rem:
            tiles.pop(r)

    return len(tiles.keys())


def run_tests():
    test_input = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""
    test_output = 2208
    assert play_game_of_life(test_input, 100) == test_output


def run() -> int:
    with open("inputs/input_24.txt") as file:
        data = file.read()
    return play_game_of_life(data, 100)


if __name__ == "__main__":
    run_tests()
    import time
    time_start = time.perf_counter()
    print(run())
    time_end = time.perf_counter() - time_start
    print(f"Time: {time_end:0.4f} sec")
