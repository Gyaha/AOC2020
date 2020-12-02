def validate_password(inp: str):
    rule, phrase = inp.split(": ")
    counts, target = rule.split(" ")
    min_, max_ = counts.split("-")
    count = phrase.count(target)
    return count >= int(min_) and count <= int(max_)


def count_valid_passwords(arr):
    r = 0
    for i in arr:
        r += validate_password(i)
    return r


test_input = ["1-3 a: abcde",
              "1-3 b: cdefg",
              "2-9 c: ccccccccc"]
test_output = 2
assert count_valid_passwords(test_input) == test_output


f = open("inputs/input_02.txt")
d = [n for n in f.readlines()]
f.close()
print(count_valid_passwords(d))
