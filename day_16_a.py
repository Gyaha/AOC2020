def read_rules(s: str) -> list:
    rules = []
    for r in s.splitlines():
        name, n = r.split(": ")
        n_l, n_r = n.split(" or ")
        n_l_l, n_l_h = [int(a) for a in n_l.split("-")]
        n_r_l, n_r_h = [int(a) for a in n_r.split("-")]
        rules.append([n_l_l, n_l_h, n_r_l, n_r_h])
    return rules


def read_tickets(s: str) -> list:
    tickets = []
    for t in s.splitlines()[1:]:
        ticket = [int(a) for a in t.split(",")]
        tickets.append(ticket)
    return tickets


def read_input(s: str) -> (list, list):
    rules, my_ticket, other_tickets = s.split("\n\n")
    rules = read_rules(rules)
    #my_ticket = read_tickets(my_ticket)
    other_tickets = read_tickets(other_tickets)
    return rules, other_tickets


def read_input_and_get_error_rate(s: str) -> int:
    rules, tickets = read_input(s)
    return get_error_rate(rules, tickets)


def validate_num_to_all_rules(n: int, rules: list) -> bool:
    for r in rules:
        if ((n >= r[0] and n <= r[1]) or (n >= r[2] and n <= r[3])):
            return True
    return False


def get_error_rate(rules: list, tickets: list) -> int:
    s = 0
    for ticket in tickets:
        for n in ticket:
            if not validate_num_to_all_rules(n, rules):
                s += n
    return s


def run_tests():
    test_input = """class: 1-3 or 5-7
    row: 6-11 or 33-44
    seat: 13-40 or 45-50

    your ticket:
    7,1,14

    nearby tickets:
    7,3,47
    40,4,50
    55,2,20
    38,6,12"""
    test_output = 71
    assert read_input_and_get_error_rate(test_input) == test_output


def run() -> int:
    with open("inputs/input_16.txt") as file:
        data = file.read()
    return read_input_and_get_error_rate(data)


if __name__ == "__main__":
    run_tests()
    print(run())
