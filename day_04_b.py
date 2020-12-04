import re


VALID_LIST = ["ecl:",
              "pid:",
              "eyr:",
              "hcl:",
              "byr:",
              "iyr:",
              # "cid:",
              "hgt:"]

VALID_EYE_COLORS = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def validate_byr(field: str):
    yr = int(field)
    return yr >= 1920 and yr <= 2002


def validate_iyr(field: str):
    yr = int(field)
    return yr >= 2010 and yr <= 2020


def validate_eyr(field: str):
    yr = int(field)
    return yr >= 2020 and yr <= 2030


def validate_hgt(field: str):
    amt, typ = field[:-2], field[-2:]
    amt = int(amt)
    if typ == "cm":
        return amt >= 150 and amt <= 193
    elif typ == "in":
        return amt >= 59 and amt <= 76
    return False


def validate_hcl(field: str):
    return re.match("#[0-9a-f]{6}", field)


def validate_ecl(field: str):
    return field in VALID_EYE_COLORS


def validate_pid(field: str):
    return re.match("[0-9]{9}$", field)


def validate_passport(passport: str):
    for v in VALID_LIST:
        if not v in passport:
            return False
    fields = re.split("\n|\s", passport)
    for field in fields:
        pre, val = field.split(":")
        if pre == "ecl":
            if not validate_ecl(val):
                return False
        elif pre == "pid":
            if not validate_pid(val):
                return False
        elif pre == "eyr":
            if not validate_eyr(val):
                return False
        elif pre == "hcl":
            if not validate_hcl(val):
                return False
        elif pre == "byr":
            if not validate_byr(val):
                return False
        elif pre == "iyr":
            if not validate_iyr(val):
                return False
        elif pre == "hgt":
            if not validate_hgt(val):
                return False
        else:
            print(pre, val)
    return True


def count_valid_passports(passport_list: str):
    passport_list = passport_list.strip()
    passports = re.split("\n\n", passport_list)
    valid_count = 0
    for passport in passports:
        valid_count += validate_passport(passport)
    return valid_count


test_input = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

test_output = 2

assert count_valid_passports(test_input) == test_output


f = open("inputs/input_04.txt")
d = f.read()
#d = [n.replace("\n", "") for n in f.readlines()]
f.close()
print(count_valid_passports(d))
