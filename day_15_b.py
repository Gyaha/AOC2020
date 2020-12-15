TARGET_TURN = 30000000


def play_memory_game(s: str) -> int:
    d = [int(a) for a in s.split(",")]
    m = {}
    t = 0
    n = 0
    tmp = 0
    for p in d:
        t += 1
        m[p] = t
    while t + 1 < TARGET_TURN:
        t += 1
        if n in m:
            tmp = t - m[n]
            m[n] = t
            n = tmp
        else:
            m[n] = t
            n = 0
    return n


test_input = "0,3,6"
test_output = 175594
assert play_memory_game(test_input) == test_output

f = open("inputs/input_15.txt")
d = f.read()
f.close()
print(play_memory_game(d))
