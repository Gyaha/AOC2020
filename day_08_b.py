def prep_inst(inst_raw: str) -> list:
    return [i for i in inst_raw.strip("\n").splitlines()]


def run_program(inst_raw: str) -> int:
    # loop debug
    ptr_list = []

    inst = prep_inst(inst_raw)
    acc = 0
    ptr = 0
    fld = False  # failed
    don = False
    while not don:
        # loop debug
        if ptr in ptr_list:
            fld = True
            don = True
            continue
        else:
            ptr_list.append(ptr)

        if ptr >= len(inst):
            don = True
            continue

        i = inst[ptr]
        c, a = i.split()
        a = int(a)
        if c == "nop":
            ptr += 1
        elif c == "acc":
            acc += a
            ptr += 1
        elif c == "jmp":
            ptr += a
        else:
            print("Command not found: " + c)
            print(acc, ptr)
            print(i, c, a)
            fld = True
            don = True
            continue
    return fld, acc


def try_swap_jmp_for_nop(s: str) -> int:
    s = s.splitlines()
    for i in range(len(s)):
        c, a = s[i].split()
        if c == "jmp":
            new_s = s.copy()
            new_s[i] = "nop +0"
            fld, acc = run_program("\n".join(new_s))
            if not fld:
                return acc


test_input = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
test_output = 8

assert try_swap_jmp_for_nop(test_input) == test_output


f = open("inputs/input_08.txt")
d = f.read()
f.close()
print(try_swap_jmp_for_nop(d))
