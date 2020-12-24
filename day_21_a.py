def indentify_ingrediens(s: str) -> dict:
    cnt = {}
    ing = {}
    for l in s.strip().strip("\n").splitlines():
        i, c = l.split(" (contains ")
        i = i.split(" ")
        c = c[:-1].split(", ")

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
                ing[j] = 1
            else:
                ing[j] += 1

    for k in cnt.keys():
        for j in cnt[k]:
            if j in ing:
                ing.pop(j)

    s = 0
    for i in ing.keys():
        s += ing[i]
    return s


def run_tests():
    test_input = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""
    test_output = 5
    assert indentify_ingrediens(test_input) == test_output


def run() -> int:
    with open("inputs/input_21.txt") as file:
        data = file.read()
    return indentify_ingrediens(data)


if __name__ == "__main__":
    run_tests()
    import time
    time_start = time.perf_counter()
    print(run())
    time_end = time.perf_counter() - time_start
    print(f"Time: {time_end:0.4f} sec")
