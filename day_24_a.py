def flip_tiles(s: str) -> int:
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
            tiles[tile] = True
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
    test_output = 10
    assert flip_tiles(test_input) == test_output


def run() -> int:
    with open("inputs/input_24.txt") as file:
        data = file.read()
    return flip_tiles(data)


if __name__ == "__main__":
    run_tests()
    import time
    time_start = time.perf_counter()
    print(run())
    time_end = time.perf_counter() - time_start
    print(f"Time: {time_end:0.4f} sec")
