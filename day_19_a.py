def count_valid_messages(s: str):
    rules, messages = s.strip().split("\n\n")
    rules = convert_rules(rules)
    messages = convert_messages(messages)
    s = 0
    for message in messages:
        s += validate_message({}, rules, [0], message)
    return s


def validate_message(memory: dict, rules: list, rule: list, message: list, depth: int = 0) -> bool:
    log = False
    pr, pm, pr1, pm1, pr2, pm2 = "", "", "", "", "", ""

    f, s = mem_get(memory, rule, message)
    if f:
        return s

    if log:
        pr = "".join([str(r) for r in rule])
        pm = "".join(message)
        print(f"{' ' * depth}? {pr} + {pm}")

    if type(rule[0]) == str:
        if len(message) == 1 and message[0] == rule[0]:
            if log:
                print(f"{' ' * depth}T {message[0]} = {rule[0]}")
            mem_set(memory, rule, message, True)
            return True
        else:
            if log:
                print(f"{' ' * depth}F {message[0]} = {rule[0]}")
            mem_set(memory, rule, message, False)
            return False

    if len(rule) > 1:
        for i in range(1, len(message) - (len(rule) - 2)):
            if log:
                pr1 = "".join([str(r) for r in [rule[0]]])
                pm1 = "".join(message[:i])
                pr2 = "".join([str(r) for r in rule[1:]])
                pm2 = "".join(message[i:])
                print(f"{' ' * depth}/ {pr1} + {pm1} / {pr2} + {pm2}")

            if validate_message(memory, rules, [rule[0]], message[:i], depth + 1) and validate_message(memory, rules, rule[1:], message[i:], depth + 1):
                if log:
                    print(f"{' ' * depth}T {pr1} + {pm1} / {pr2} + {pm2}")

                mem_set(memory, rule, message, True)
                return True

    else:
        r = rules[rule[0]]
        if len(r) > 1:
            for i in range(len(r)):
                if log:
                    pr1 = "".join([str(r) for r in r[i]])
                    pm1 = "".join(message)
                    print(f"{' ' * depth}< {pr1} + {pm1}")

                if validate_message(memory, rules, r[i], message, depth + 1):
                    if log:
                        print(f"{' ' * depth}T {pr1} + {pm1}")

                    mem_set(memory, rule, message, True)
                    return True
        else:
            return validate_message(memory, rules, r[0], message, depth + 1)
    if log:
        print(f"{' ' * depth}F {pr} + {pm}")
    mem_set(memory, rule, message, False)
    return False


def mem_get(memory: dict, rule: list, message: list) -> (bool, bool):
    log = False
    i = "_".join([str(r) for r in rule]) + "".join(message)
    if i in memory:
        if log:
            print(f"mem_fnd - {i} - {memory[i]}")
        return True, memory[i]
    else:
        return False, False


def mem_set(memory: dict, rule: list, message: list, status: bool):
    log = False
    i = "_".join([str(r) for r in rule]) + "".join(message)
    if i in memory:
        print(f"ERROR: {i} is in mem")
    if log:
        print(f"mem_set: {i} - {status}")
    memory[i] = status


def convert_rules(rules: str) -> list:
    rule_lines = rules.splitlines()
    r = [[] for _ in rule_lines]
    for rule in rule_lines:
        rule_id, rule_text = rule.strip().split(": ")
        rule_id = int(rule_id)
        rule_text = convert_rule_text(rule_text)
        r[rule_id] = rule_text
    return r


def convert_rule_text(s: str) -> list:
    l = []
    l2 = []
    for c in s.split(" "):
        if c.isnumeric():
            l2.append(int(c))
        elif "\"" in c:
            l2.append(c[1])
        else:  # |
            l.append(l2)
            l2 = []
    l.append(l2)
    return l


def convert_messages(messages: str) -> list:
    m = [list(i.strip()) for i in messages.splitlines()]
    return m


def run_tests():
    test_input = """0: 4 1 5
    1: 2 3 | 3 2
    2: 4 4 | 5 5
    3: 4 5 | 5 4
    4: "a"
    5: "b"

    ababbb
    bababa
    abbbab
    aaabbb
    aaaabbb"""
    test_output = 2
    assert count_valid_messages(test_input) == test_output


def run() -> int:
    with open("inputs/input_19.txt") as file:
        data = file.read()
    return count_valid_messages(data)


if __name__ == "__main__":
    run_tests()
    print(run())
