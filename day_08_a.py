def prep_inst(inst_raw: str) -> list:
    return [i for i in inst_raw.strip("\n").splitlines()]


def run_program(inst_raw: str) -> int:
    # loop debug
    ptr_list = []

    inst = prep_inst(inst_raw)
    acc = 0
    ptr = 0
    don = 0
    while not don:
        # loop debug
        if ptr in ptr_list:
            don = True
            continue
        else:
            ptr_list.append(ptr)

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
            don = True
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
test_output = 5

assert run_program(test_input) == test_output


f = open("inputs/input_08.txt")
d = f.read()
f.close()
print(run_program(d))
