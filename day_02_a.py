def validate_password(inp: str):
    rule, phrase = inp.split(": ")
    counts, target = rule.split(" ")
    min_, max_ = counts.split("-")


test_input = ["1-3 a: abcde",
              "1-3 b: cdefg",
              "2-9 c: ccccccccc"]
test_output = 2


validate_password(test_input[0])
