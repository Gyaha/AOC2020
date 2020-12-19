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
            count = int(b_split[0])
            name = " ".join(b_split[1:3])
            contained_list.append([name, count])
        rules[current_bag] = contained_list
    return rules


def count_content(rules: dict, target: str) -> int:
    t = rules[target]
    r = 1
    for a in t:
        r += a[1] * count_content(rules, a[0])
    return r


def count_contents(rules: dict, target: str) -> int:
    return count_content(rules, target) - 1


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
    test_output = 32

    assert count_contents(create_rules(test_input), "shiny gold") == test_output

    test_input = """shiny gold bags contain 2 dark red bags.
    dark red bags contain 2 dark orange bags.
    dark orange bags contain 2 dark yellow bags.
    dark yellow bags contain 2 dark green bags.
    dark green bags contain 2 dark blue bags.
    dark blue bags contain 2 dark violet bags.
    dark violet bags contain no other bags."""
    test_output = 126

    assert count_contents(create_rules(test_input), "shiny gold") == test_output


def run() -> int:
    with open("inputs/input_07.txt") as file:
        data = file.read()
    return count_contents(create_rules(data), TARGET)


if __name__ == "__main__":
    run_tests()
    print(run())
