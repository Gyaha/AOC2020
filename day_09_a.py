def test_preamble(l: list) -> bool:
    t = l.pop()
    for i in range(len(l) - 1):
        if t - l[i] in l[i + 1:]:
            return True
    return False


def find_preamble(s: str, p: int) -> int:
    l = [int(l) for l in s.splitlines()]
    for i in range(len(l) - p):
        if not test_preamble(l[i:i + p + 1]):
            return l[i + p]


test_input = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""
test_output = 127
assert find_preamble(test_input, 5) == test_output


f = open("inputs/input_09.txt")
d = f.read()
f.close()
print(find_preamble(d, 25))
