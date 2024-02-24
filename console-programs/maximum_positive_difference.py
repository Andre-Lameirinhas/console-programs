import math
import random
import time

list_size = 10_000
random_list = [random.randint(1, 10_000) for _ in range(list_size)]


def double_loop() -> int:
    print("using double loop approach")
    max_diff = 0

    for pos, x in enumerate(random_list):
        for y in random_list[:pos]:
            if x - y > max_diff:
                max_diff = x - y

    return max_diff


def calc_min() -> int:
    print("using calc min approach")
    max_diff = 0

    for pos, x in enumerate(random_list):
        if pos == 0:
            continue

        min_value = min(random_list[:pos])
        if x - min_value > max_diff:
            max_diff = x - min_value

    return max_diff


def storing_min() -> int:
    print("using storing min approach")
    max_diff = 0
    min_value = math.inf

    for x in random_list:
        if x < min_value:
            min_value = x

        if x - min_value > max_diff:
            max_diff = x - min_value

    return max_diff


functions = [double_loop, calc_min, storing_min]

for function in functions:
    start = time.perf_counter_ns()
    res = function()
    end = time.perf_counter_ns()
    print(f"max positive diference = {res}")
    print(f"elapsed time: {(end - start) / 1000000} ms")
    print()
