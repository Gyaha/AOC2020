def find_sum_in_range(s: str, target: int) -> int:
    l = [int(l) for l in s.splitlines()]
    for i in range(len(l)):
        for o in range(2, len(l) - i):
            if sum(l[i:i + o]) == target:
                return min(l[i:i + o]) + max(l[i:i + o])


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
test_input_2 = 127
test_output = 62
assert find_sum_in_range(test_input, test_input_2) == test_output


f = open("inputs/input_09.txt")
d = f.read()
f.close()
print(find_sum_in_range(d, 32321523))
