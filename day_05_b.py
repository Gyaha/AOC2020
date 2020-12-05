def translate_row(inp: str) -> int:
    b = "0b" + (inp.replace("F", "0").replace("B", "1"))
    return int(b, 2)


def translate_column(inp: str) -> int:
    b = "0b" + (inp.replace("L", "0").replace("R", "1"))
    return int(b, 2)


def translate_pass_to_seat(inp: str) -> int:
    return (translate_row(inp[:-3]) * 8) + translate_column(inp[-3:])


def get_seat_list(arr) -> list:
    return [translate_pass_to_seat(p) for p in arr]


def get_centered_seat(arr) -> int:
    list_of_seats = sorted(get_seat_list(arr))
    last = 0
    for seat in list_of_seats:
        if last + 2 == seat:
            return last + 1
        last = seat


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
print(get_centered_seat(d))
