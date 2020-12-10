def count_adapter_possibilities(s: str) -> int:
    l = sorted([int(l) for l in s.strip("\n").splitlines()])
    p2, p3 = 0, 0
    for i in range(len(l)-2):
        if (l[i+2] - l[i] <= 3):
            p2 += 1
        if i+3 >= len(l):
            continue
        if (l[i+3] - l[i] <= 3):
            p3 += 1
    print(p2, p3)

    r = (p2 + p3) ** 2
    print(r)
    return r


test_input = """16
10
15
5
1
11
7
19
6
12
4"""
test_output = 8

assert count_adapter_possibilities(test_input) == test_output

test_input = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""
test_output = 19208

assert count_adapter_possibilities(test_input) == test_output


f = open("inputs/input_10.txt")
d = f.read()
f.close()
print(count_adapter_possibilities(d))
