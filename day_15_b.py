TARGET_TURN = 30000000


def play_memory_game(s: str) -> int:
    d = [int(a) for a in s.split(",")]
    m = {}
    t = 0
    n = 0
    f = True
    for p in d:
        t += 1
        m[p] = t
    while t + 1 < TARGET_TURN:
        t += 1
        m, n = do_turn(m, n, t)
    return n


def do_turn(m: dict, n: int, t: int):
    if n in m:
        tmp = t - m[n]
        m[n] = t
        n = tmp
    else:
        m[n] = t
        n = 0
    return m, n


test_input = "0,3,6"
test_output = 175594
assert play_memory_game(test_input) == test_output

print("test 1")

test_input = "1,3,2"
test_output = 2578
assert play_memory_game(test_input) == test_output

print("test 2")

test_input = "2,1,3"
test_output = 3544142
assert play_memory_game(test_input) == test_output

print("test 3")

test_input = "1,2,3"
test_output = 261214
assert play_memory_game(test_input) == test_output

print("test 4")

test_input = "2,3,1"
test_output = 6895259
assert play_memory_game(test_input) == test_output

print("test 5")

test_input = "3,2,1"
test_output = 18
assert play_memory_game(test_input) == test_output

print("test 6")

test_input = "3,1,2"
test_output = 362
assert play_memory_game(test_input) == test_output

print("test 7")

f = open("inputs/input_15.txt")
d = f.read()
f.close()
print(play_memory_game(d))
