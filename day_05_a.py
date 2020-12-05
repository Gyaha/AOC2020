def translate_row(inp: str) -> int:
    b = "0b" + (inp.replace("F", "0").replace("B", "1"))
    return int(b, 2)


def translate_column(inp: str) -> int:
    b = "0b" + (inp.replace("L", "0").replace("R", "1"))
    return int(b, 2)


def translate_pass_to_seat(inp: str) -> int:
    return (translate_row(inp[:-3]) * 8) + translate_column(inp[-3:])


def get_higest_seat(arr) -> int:
    h = 0
    for p in arr:
        seat = translate_pass_to_seat(p)
        if seat > h:
            h = seat
    return h


test_input = "FBFBBFF"
test_output = 44
assert translate_row(test_input) == test_output

test_input = "BBFFBBF"
test_output = 102
assert translate_row(test_input) == test_output

test_input = "RLR"
test_output = 5
assert translate_column(test_input) == test_output

test_input = "RLL"
test_output = 4
assert translate_column(test_input) == test_output

test_input = "BFFFBBFRRR"
test_output = 567
assert translate_pass_to_seat(test_input) == test_output


f = open("inputs/input_05.txt")
d = [n.replace("\n", "") for n in f.readlines()]
f.close()
print(get_higest_seat(d))
