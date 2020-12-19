import re


VALID_LIST = ["ecl:",
              "pid:",
              "eyr:",
              "hcl:",
              "byr:",
              "iyr:",
              # "cid:",
              "hgt:"]


def validate_passport(passport: str):
    fields = re.findall("[a-z]{3}:", passport)
    for v in VALID_LIST:
        if not v in fields:
            return False
    return True


def count_valid_passports(passport_list: str):
    passport_list = passport_list.strip()
    passports = re.split("\n\n", passport_list)
    valid_count = 0
    for passport in passports:
        valid_count += validate_passport(passport)
    return valid_count


def run_tests():
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


def run() -> int:
    with open("inputs/input_04.txt") as file:
        data = file.read()
    return count_valid_passports(data)


if __name__ == "__main__":
    run_tests()
    print(run())
