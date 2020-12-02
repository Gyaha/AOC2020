def validate_password(inp: str):
    rule, phrase = inp.split(": ")
    phrase = list(phrase)
    ids, target = rule.split(" ")
    id_1, id_2 = ids.split("-")
    id_1, id_2 = int(id_1), int(id_2)
    return (phrase[id_1 - 1] == target) != (phrase[id_2 - 1] == target)


def count_valid_passwords(arr):
    r = 0
    for i in arr:
        r += validate_password(i)
    return r


test_input = ["1-3 a: abcde",
              "1-3 b: cdefg",
              "2-9 c: ccccccccc"]
test_output = 1
assert count_valid_passwords(test_input) == test_output


f = open("inputs/input_02.txt")
d = [n for n in f.readlines()]
f.close()
print(count_valid_passwords(d))
