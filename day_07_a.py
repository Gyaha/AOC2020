TARGET = "shiny gold"


def create_rules(s: str) -> dict:
    rules = {}
    for l in s.strip("\n").split("\n"):
        current_bag, contained_bags = l.strip().split(" bags contain ")
        contained_list = []
        for b in contained_bags.split(", "):
            if b == "no other bags.":
                continue
            b_split = b.split(" ")
            name = " ".join(b_split[1:3])
            contained_list.append(name)
        rules[current_bag] = contained_list
    return rules


def create_reverse_rules(s: str) -> dict:
    rules = create_rules(s)
    new_rules = {}
    for r in rules:
        l = rules[r]
        for rl in l:
            if not rl in new_rules:
                new_rules[rl] = []
            if not r in new_rules[rl]:
                new_rules[rl].append(r)
    return new_rules


def list_with_reverse_rules(rules: dict, target: str) -> list:
    a = [target]
    if target not in rules:
        return a
    for t in rules[target]:
        a += list_with_reverse_rules(rules, t)
    return a


def count_with_reverse_rules(rules: dict, target: str) -> int:
    return len(set(list_with_reverse_rules(rules, target))) - 1


def run_tests():
    test_input = """light red bags contain 1 bright white bag, 2 muted yellow bags.
    dark orange bags contain 3 bright white bags, 4 muted yellow bags.
    bright white bags contain 1 shiny gold bag.
    muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
    shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
    dark olive bags contain 3 faded blue bags, 4 dotted black bags.
    vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
    faded blue bags contain no other bags.
    dotted black bags contain no other bags."""
    test_output = 4

    assert count_with_reverse_rules(create_reverse_rules(test_input), TARGET) == test_output


def run() -> int:
    with open("inputs/input_07.txt") as file:
        data = file.read()
    return count_with_reverse_rules(create_reverse_rules(data), TARGET)


if __name__ == "__main__":
    run_tests()
    print(run())
