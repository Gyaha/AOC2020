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
    my_ticket = read_tickets(my_ticket)
    other_tickets = read_tickets(other_tickets)
    return rules, other_tickets + my_ticket


def discard_invalid_tickets(tickets: list, rules: list) -> list:
    r = []
    for t in tickets:
        if validate_ticket_to_all_rules(t, rules):
            r.append(t)
    return r


def validate_ticket_to_all_rules(ticket: list, rules: list) -> bool:
    for n in ticket:
        if not validate_number_to_all_rules(n, rules):
            return False
    return True


def validate_number_to_all_rules(n: int, rules: list) -> bool:
    for r in rules:
        if validate_number_to_rule(n, r):
            return True
    return False


def validate_row_rules(tickets: list, rules: list) -> dict:
    valid_row_rules = {}
    for row in range(len(rules)):
        for rule in range(len(rules)):
            if validate_row_on_rule(tickets, rules[rule], row):
                if not row in valid_row_rules:
                    valid_row_rules[row] = []
                valid_row_rules[row].append(rule)
    return valid_row_rules


def validate_row_on_rule(tickets: list, rule: list, row: int):
    for t in tickets:
        if not validate_number_to_rule(t[row], rule):
            return False
    return True


def validate_tickets_to_rules_in_order(tickets: list, rules: list, order: list) -> bool:
    for t in tickets:
        if not validate_ticket_to_rules_in_order(t, rules, order):
            return False
    return True


def validate_ticket_to_rules_in_order(ticket: list, rules: list, order: list) -> bool:
    for ti, ri in enumerate(order):
        if not validate_number_to_rule(ticket[ti], rules[ri]):
            return False
    return True


def validate_number_to_rule(n: int, r: list) -> bool:
    return ((n >= r[0] and n <= r[1]) or (n >= r[2] and n <= r[3]))


def get_valid_ticket_row_permutaitions(s: str):
    rules, tickets = read_input(s)
    tickets = discard_invalid_tickets(tickets, rules)
    valid_row_rules = validate_row_rules(tickets, rules)
    condence_valid_row_rules(valid_row_rules)
    valid_permutations = get_valid_row_permutations(valid_row_rules, 0, [0] * len(rules), [])
    return valid_permutations


def get_valid_row_permutations(valid_row_rules: dict, i: int, per: list, l: list) -> list:
    if i >= len(per):
        l.append(per.copy())
        return
    for j in valid_row_rules[i]:
        if not j in per[:i]:
            per[i] = j
            get_valid_row_permutations(valid_row_rules, i + 1, per, l)
    return l


def condence_valid_row_rules(valid_row_rules: dict):
    done = False
    while not done:
        done = True
        for rule, i in enumerate(valid_row_rules):
            if len(valid_row_rules[i]) == 1:
                if remove_row_from_other_rules(valid_row_rules, valid_row_rules[i][0], rule):
                    done = False


def remove_row_from_other_rules(valid_row_rules: dict, n: int, r: int):
    removed = False
    for rule, i in enumerate(valid_row_rules):
        if rule == r:
            continue
        if n in valid_row_rules[i]:
            removed = True
            valid_row_rules[i].remove(n)
    return removed


def get_target_rules(s: str, t: str) -> list:
    r = []
    for i, s in enumerate(s.splitlines()):
        if t in s:
            r.append(i)
    return r


def validate_ticket(s: str, t: str):
    rule_order = get_valid_ticket_row_permutaitions(s)[0]

    rules, my_ticket, other_tickets = s.split("\n\n")
    target_rules = get_target_rules(rules, t)
    my_ticket_data = read_tickets(my_ticket)[0]

    s = 0
    for i, j in enumerate(rule_order):
        if j in target_rules:
            if s == 0:
                s = my_ticket_data[i]
            else:
                s *= my_ticket_data[i]
    return s


test_input = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""
test_output = [[1, 0, 2]]
assert get_valid_ticket_row_permutaitions(test_input) == test_output


f = open("inputs/input_16.txt")
d = f.read()
f.close()
print(validate_ticket(d, "departure"))
