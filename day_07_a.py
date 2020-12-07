def create_rules(s: str) -> dict:
    rules = {}
    for l in s.split("\n"):
        current_bag, contained_bags = l.split(" bags contain ")
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


def list_holder(rules: dict, target: str) -> list:
    r = []
    for b in rules:
        for n in rules[b]:
            if n[0] == target:
                r.append(b)
    return r


def list_holders(rules: dict, target: str) -> list:
    r = []
    r += list_holder(rules, target)
    for h in r:
        r += list_holders(rules, h)
    return r


def count_holders(rules: dict, target: str) -> int:
    return len(set(list_holders(rules, target)))


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

assert count_holders(create_rules(test_input), "shiny gold") == test_output


f = open("inputs/input_07.txt")
d = f.read().strip("\n")
f.close()
print(count_holders(create_rules(d), "shiny gold"))
