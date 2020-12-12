def move_direction(x, y, vx, vy, n) -> (int, int):
    x += vx * n
    y += vy * n
    return x, y


def move_target(vx, vy, d, n):
    if d == "E":
        vx += n
    elif d == "W":
        vx -= n
    elif d == "S":
        vy -= n
    else:  # "N"
        vy += n
    return vx, vy


def rotate_direction(vx, vy, w, n) -> (int, int):
    while n > 0:
        n -= 90
        tx, ty = vx, vy
        if w == "L":
            vx = -ty
            vy = tx
        else:  # "R"
            vx = ty
            vy = -tx
    return vx, vy


assert rotate_direction(10, 4, "R", 90) == (4, -10)
assert rotate_direction(10, 4, "L", 90) == (-4, 10)


def manhatten_dist(x: int, y: int) -> int:
    return abs(x) + abs(y)


def stumble_about(s: str) -> (int, int):
    l = [a for a in s.splitlines()]
    x, y = 0, 0
    vx, vy = 10, 1
    for a in l:
        b, n = a[0], int(a[1:])
        if b == "F":
            x, y = move_direction(x, y, vx, vy, n)
        elif b == "R" or b == "L":
            vx, vy = rotate_direction(vx, vy, b, n)
        else:  # "EWSN"
            vx, vy = move_target(vx, vy, b, n)
    return x, y


def stumble_about_manhatten(s: str) -> int:
    x, y = stumble_about(s)
    return manhatten_dist(x, y)


test_input = """F10
N3
F7
R90
F11"""
test_output = 286
assert stumble_about_manhatten(test_input) == test_output


f = open("inputs/input_12.txt")
d = f.read()
f.close()
print(stumble_about_manhatten(d))
