def read_fields(s: str) -> list:
    fields = []
    for r in s.splitlines():
        name, n = r.split(": ")
        n_l, n_r = n.split(" or ")
        n_l_l, n_l_h = [int(a) for a in n_l.split("-")]
        n_r_l, n_r_h = [int(a) for a in n_r.split("-")]
        fields.append([n_l_l, n_l_h, n_r_l, n_r_h])
    return fields


def read_target_fields(s: str, t: str) -> list:
    r = []
    for i, s in enumerate(s.splitlines()):
        if t in s:
            r.append(i)
    return r


def read_tickets(s: str) -> list:
    tickets = []
    for t in s.splitlines()[1:]:
        ticket = [int(a) for a in t.split(",")]
        tickets.append(ticket)
    return tickets


def discard_invalid(tickets: list, rules: list) -> list:
    valid_tickets = []
    for ticket in tickets:
        if validate_ticket_all_fields(ticket, rules):
            valid_tickets.append(ticket)
    return valid_tickets


def validate_ticket_all_fields(ticket: list, fields: list) -> bool:
    for v in ticket:
        if not validate_value_all_fields(v, fields):
            return False
    return True


def validate_value_all_fields(v: int, fields: list) -> bool:
    for f in fields:
        if validate_value_field(v, f):
            return True
    return False


def validate_value_field(v: int, f: list) -> bool:
    return ((v >= f[0] and v <= f[1]) or (v >= f[2] and v <= f[3]))


def validate_field_rows(tickets: list, fields: list) -> list:
    valid_field_rows = [[] for _ in range(len(fields))]
    for row in range(len(fields)):
        for field in range(len(fields)):
            if validate_field_row(tickets, fields[field], row):
                valid_field_rows[row].append(field)
    return valid_field_rows


def validate_field_row(tickets: list, field: list, row: int) -> bool:
    for ticket in tickets:
        if not validate_value_field(ticket[row], field):
            return False
    return True


def condence_valid_field_rows(valid_field_rows: list) -> list:
    done = False
    while not done:
        done = True
        for i, rows in enumerate(valid_field_rows):
            if len(rows) == 1:
                if condence_extra_rows(valid_field_rows, rows[0], i):
                    done = False
    return valid_field_rows


def condence_extra_rows(valid_field_rows: list, v: int, i: int):
    removed = False
    for j, rows in enumerate(valid_field_rows):
        if j == i:
            continue
        if v in rows:
            rows.remove(v)
            removed = True
    return removed


def valid_field_row_permutations(valid_field_rows: list, i: int, per: list, l: list) -> list:
    if i >= len(per):
        l.append(per.copy())
        return
    for j in valid_field_rows[i]:
        if not j in per[:i]:
            per[i] = j
            valid_field_row_permutations(valid_field_rows, i + 1, per, l)
    return l


def validate_ticket(s: str, t: str) -> int:
    fields, my_ticket, nearby_tickets = s.split("\n\n")
    target_fields = read_target_fields(fields, t)
    fields = read_fields(fields)
    my_ticket = read_tickets(my_ticket)
    nearby_tickets = discard_invalid(read_tickets(nearby_tickets), fields)
    valid_field_rows = condence_valid_field_rows(validate_field_rows(my_ticket + nearby_tickets, fields))
    valid_field_permutations = valid_field_row_permutations(valid_field_rows, 0, [0] * len(fields), [])
    if len(valid_field_permutations) > 1:
        print("ERROR: multiple valid results")
    valid_field_permutation = valid_field_permutations[0]
    return validate_fields(valid_field_permutation, target_fields, my_ticket[0])


def validate_fields(valid_field_permutation, target_fields, my_ticket) -> int:
    s = 0
    for i, j in enumerate(valid_field_permutation):
        if j in target_fields:
            if s == 0:
                s = my_ticket[i]
            else:
                s *= my_ticket[i]
    return s


def run_tests():
    test_input = """class: 0-1 or 4-19
    row: 0-5 or 8-19
    seat: 0-13 or 16-19

    your ticket:
    11,12,13

    nearby tickets:
    3,9,18
    15,1,5
    5,14,9"""
    test_input2 = "row"
    test_output = 11
    assert validate_ticket(test_input, test_input2) == test_output


def run() -> int:
    with open("inputs/input_16.txt") as file:
        data = file.read()
    return validate_ticket(data, "departure")


if __name__ == "__main__":
    run_tests()
    print(run())
