def find_evil_ingredients(s: str) -> dict:
    cnt = {}
    ing = []
    recipes = []
    for l in s.strip().strip("\n").splitlines():
        i, c = l.split(" (contains ")
        i = i.split(" ")
        c = c[:-1].split(", ")
        recipes.append([i, c])
        for k in c:
            if not k in cnt:
                cnt[k] = [j for j in i]
            else:
                for j in cnt[k]:
                    if not j in i:
                        cnt[k].remove(j)

        for k in c:
            for j in cnt[k]:
                if not j in i:
                    cnt[k].remove(j)

        for j in i:
            if not j in ing:
                ing.append(j)

    for k in cnt.keys():
        for j in cnt[k]:
            if j in ing:
                ing.remove(j)

    for r in recipes:
        for j in r[0]:
            if j in ing:
                r[0].remove(j)

    pos = {}
    for r in recipes:
        for c in r[1]:
            if not c in pos:
                pos[c] = [j for j in r[0]]
            else:
                for i in pos[c]:
                    if not i in r[0]:
                        pos[c].remove(i)

    condence_pos(pos)

    evil_ing = []

    for c in sorted(pos.keys()):
        evil_ing.append(pos[c][0])

    return ",".join(evil_ing)


def condence_pos(pos: dict):
    done = False
    while not done:
        done = True
        for r in pos.keys():
            if len(pos[r]) == 1:
                if not remove_ing_from_other(pos, pos[r][0], r):
                    done = False
                    break


def remove_ing_from_other(pos: dict, i: str, oc: str) -> bool:
    done = True
    for c in pos.keys():
        if c == oc:
            continue
        if i in pos[c]:
            pos[c].remove(i)
            done = False
    return done


def run_tests():
    test_input = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""
    test_output = "mxmxvkd,sqjhc,fvjkl"
    assert find_evil_ingredients(test_input) == test_output


def run() -> int:
    with open("inputs/input_21.txt") as file:
        data = file.read()
    return find_evil_ingredients(data)


if __name__ == "__main__":
    run_tests()
    import time
    time_start = time.perf_counter()
    print(run())
    time_end = time.perf_counter() - time_start
    print(f"Time: {time_end:0.4f} sec")
