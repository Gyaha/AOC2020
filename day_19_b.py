def count_valid_messages(s: str):
    rules, messages = s.strip().split("\n\n")
    rules = convert_rules(rules)
    inject_rules(rules, [[8, [[42], [42, 8]]], [11, [[42, 31], [42, 11, 31]]]])
    messages = convert_messages(messages)
    s = 0
    for message in messages:
        s += validate_message({}, rules, [0], message)
    return s


def inject_rules(rules: list, new_rules: list):
    for nr in new_rules:
        rules[nr[0]] = nr[1]


def validate_message(memory: dict, rules: list, rule: list, message: list) -> bool:
    if rule[0] < 0:
        return len(message) == 1 and message[0] == rule[0]

    f, s = mem_get(memory, rule, message)
    if f:
        return s

    if len(rule) > 1:
        for i in range(1, len(message) - (len(rule) - 2)):
            if validate_message(memory, rules, [rule[0]], message[:i]) and validate_message(memory, rules, rule[1:], message[i:]):
                mem_set(memory, rule, message, True)
                return True
    else:
        r = rules[rule[0]]
        if len(r) > 1:
            for i in range(len(r)):
                if validate_message(memory, rules, r[i], message):
                    mem_set(memory, rule, message, True)
                    return True
        else:
            return validate_message(memory, rules, r[0], message)

    mem_set(memory, rule, message, False)
    return False


def mem_get(memory: dict, rule: list, message: list) -> (bool, bool):
    i = tuple(rule + [-3] + message)
    if not (m := memory.get(i, -3)) == -3:
        return True, m
    else:
        return False, False


def mem_set(memory: dict, rule: list, message: list, status: bool):
    i = tuple(rule + [-3] + message)
    memory[i] = status


def convert_rules(rules: str) -> list:
    rule_lines = rules.splitlines()
    r = []
    for rule in rule_lines:
        rule_id, rule_text = rule.strip().split(": ")
        rule_id = int(rule_id)
        rule_text = convert_rule_text(rule_text)
        while len(r) <= rule_id:
            r.append([])
        r[rule_id] = rule_text
    return r


def convert_rule_text(s: str) -> list:
    l = []
    l2 = []
    for c in s.split(" "):
        if c.isnumeric():
            l2.append(int(c))
        elif "\"" in c:
            if c[1] == "a":
                l2.append(-1)
            else:
                l2.append(-2)
        else:  # |
            l.append(l2)
            l2 = []
    l.append(l2)
    return l


def convert_messages(messages: str) -> list:
    m = [[-1 if j == "a" else -2 for j in i] for i in [list(i.strip()) for i in messages.splitlines()]]
    return m


def run_tests():
    test_input = """42: 9 14 | 10 1
    9: 14 27 | 1 26
    10: 23 14 | 28 1
    1: "a"
    11: 42 31
    5: 1 14 | 15 1
    19: 14 1 | 14 14
    12: 24 14 | 19 1
    16: 15 1 | 14 14
    31: 14 17 | 1 13
    6: 14 14 | 1 14
    2: 1 24 | 14 4
    0: 8 11
    13: 14 3 | 1 12
    15: 1 | 14
    17: 14 2 | 1 7
    23: 25 1 | 22 14
    28: 16 1
    4: 1 1
    20: 14 14 | 1 15
    3: 5 14 | 16 1
    27: 1 6 | 14 18
    14: "b"
    21: 14 1 | 1 14
    25: 1 1 | 1 14
    22: 14 14
    8: 42
    26: 14 22 | 1 20
    18: 15 15
    7: 14 5 | 1 21
    24: 14 1

    abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
    bbabbbbaabaabba
    babbbbaabbbbbabbbbbbaabaaabaaa
    aaabbbbbbaaaabaababaabababbabaaabbababababaaa
    bbbbbbbaaaabbbbaaabbabaaa
    bbbababbbbaaaaaaaabbababaaababaabab
    ababaaaaaabaaab
    ababaaaaabbbaba
    baabbaaaabbaaaababbaababb
    abbbbabbbbaaaababbbbbbaaaababb
    aaaaabbaabaaaaababaa
    aaaabbaaaabbaaa
    aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
    babaaabbbaaabaababbaabababaaab
    aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"""
    test_output = 12
    assert count_valid_messages(test_input) == test_output


def run() -> int:
    with open("inputs/input_19.txt") as file:
        data = file.read()
    return count_valid_messages(data)


if __name__ == "__main__":
    run_tests()
    import time
    time_start = time.perf_counter()
    print(run())
    time_end = time.perf_counter() - time_start
    print(f"Time: {time_end:0.4f} sec")
