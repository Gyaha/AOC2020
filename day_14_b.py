def find_all_memory_adresses(bitmask: list, t: int) -> list:
    nt = [0] * 36
    bt = list(bin(t)[2:].zfill(36))
    for i, m, d in zip(range(36), bitmask, bt):
        if m == "0":
            nt[i] = bt[i]
        elif m == "1":
            nt[i] = "1"
        else:  # "X"
            nt[i] = "X"
    # print("".join(nt))
    return build_multi_list(nt, 0, [])


def build_multi_list(mem: list, i: int, l: list) -> list:
    if i == len(mem):
        l.append(mem)
        return l
    if mem[i] == "X":
        m0 = mem.copy()
        m0[i] = "0"
        build_multi_list(m0, i + 1, l)
        m1 = mem.copy()
        m1[i] = "1"
        build_multi_list(m1, i + 1, l)
        return l
    else:
        return build_multi_list(mem, i + 1, l)


def insert_data_into_multi_memory(memory: dict, bitmask: list, t: int, b: list):
    memory_addresses = find_all_memory_adresses(bitmask, t)
    for m in memory_addresses:
        #print("".join(m), int("".join(m), 2))
        memory[int("".join(m), 2)] = b


def read_docking_data(s: str):
    d = [l for l in s.strip("\n").splitlines()]
    bitmask = None
    memory = {}
    for l in d:
        s, e = l.split(" = ")
        if s == "mask":
            bitmask = list(e)
        else:
            t = int("".join(list(s)[4:-1]))
            b = list(bin(int(e))[2:].zfill(36))
            insert_data_into_multi_memory(memory, bitmask, t, b)
    s = 0
    for i in memory:
        s += int("".join(memory[i]), 2)
    return s


test_input = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""
test_output = 208
assert read_docking_data(test_input) == test_output


f = open("inputs/input_14.txt")
d = f.read()
f.close()
print(read_docking_data(d))
