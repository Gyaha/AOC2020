import time
import day_01_a
import day_01_b
import day_02_a
import day_02_b
import day_03_a
import day_03_b
import day_04_a
import day_04_b
import day_05_a
import day_05_b
import day_06_a
import day_06_b
import day_07_a
import day_07_b
import day_08_a
import day_08_b
import day_09_a
import day_09_b
import day_10_a
import day_10_b
import day_11_a
import day_11_b
import day_12_a
import day_12_b
import day_13_a
import day_13_b
import day_14_a
import day_14_b
import day_15_a
import day_15_b
import day_16_a
import day_16_b
import day_17_a
import day_17_b
import day_18_a
import day_18_b
import day_19_a
import day_19_b
import day_20_a
import day_20_b
import day_21_a
import day_21_b
import day_22_a
import day_22_b
import day_23_a
import day_23_b
import day_24_a
import day_24_b
import day_25_a

import day_15


def time_day(i: str, a_run, b_run) -> float:
    time_start = time.perf_counter()
    a_run()
    time_a = time.perf_counter() - time_start
    time_start = time.perf_counter()
    if b_run != None:
        b_run()
    time_b = time.perf_counter() - time_start
    time_total = time_a + time_b
    print(f"{i}\t{time_a:0.2f}\t{time_b:0.2f}\t{time_total:0.4f}")
    return time_total


def time_days():
    print("ADVENT OF CODE 2020")
    print("Day\tA\tB\tTotal")
    time_total = 0
    time_total += time_day("01", day_01_a.run, day_01_b.run)
    time_total += time_day("02", day_02_a.run, day_02_b.run)
    time_total += time_day("03", day_03_a.run, day_03_b.run)
    time_total += time_day("04", day_04_a.run, day_04_b.run)
    time_total += time_day("05", day_05_a.run, day_05_b.run)
    time_total += time_day("06", day_06_a.run, day_06_b.run)
    time_total += time_day("07", day_07_a.run, day_07_b.run)
    time_total += time_day("08", day_08_a.run, day_08_b.run)
    time_total += time_day("09", day_09_a.run, day_09_b.run)
    time_total += time_day("10", day_10_a.run, day_10_b.run)
    time_total += time_day("11", day_11_a.run, day_11_b.run)
    time_total += time_day("12", day_12_a.run, day_12_b.run)
    time_total += time_day("13", day_13_a.run, day_13_b.run)
    time_total += time_day("14", day_14_a.run, day_14_b.run)
    time_total += time_day("15", day_15_a.run, day_15_b.run)
    time_total += time_day("+c", day_15.run_a, day_15.run_b)
    time_total += time_day("16", day_16_a.run, day_16_b.run)
    time_total += time_day("17", day_17_a.run, day_17_b.run)
    time_total += time_day("18", day_18_a.run, day_18_b.run)
    time_total += time_day("19", day_19_a.run, day_19_b.run)
    time_total += time_day("20", day_20_a.run, day_20_b.run)
    time_total += time_day("21", day_21_a.run, day_21_b.run)
    time_total += time_day("22", day_22_a.run, day_22_b.run)
    time_total += time_day("23", day_23_a.run, day_23_b.run)
    time_total += time_day("24", day_24_a.run, day_24_b.run)
    time_total += time_day("25", day_25_a.run, None)
    print(f"Total - {time_total:0.4f} sec")


if __name__ == "__main__":
    time_days()
