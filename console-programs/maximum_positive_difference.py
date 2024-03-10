import math
import sys
import random
import time
from typing import List


def double_loop(list_: List) -> int:
    print("Using double loop approach")
    max_diff = 0

    for pos, x in enumerate(list_):
        for y in list_[:pos]:
            if x - y > max_diff:
                max_diff = x - y

    return max_diff


def calc_min(list_: List) -> int:
    print("Using calc min approach")
    max_diff = 0

    for pos, x in enumerate(list_):
        if pos == 0:
            continue

        min_value = min(list_[:pos])
        if x - min_value > max_diff:
            max_diff = x - min_value

    return max_diff


def store_min(list_: List) -> int:
    print("Using store min approach")
    max_diff = 0
    min_value = math.inf

    for x in list_:
        if x < min_value:
            min_value = x

        if x - min_value > max_diff:
            max_diff = x - min_value

    return max_diff


if __name__ == "__main__":
    list_size = 10_000
    try:
        if len(sys.argv) > 1:
            list_size = int(sys.argv[1])
    except ValueError:
        print("Invalid list size")
        exit(1)

    print(f"Calculating Maximum Positive Difference for a list of {list_size} elements")

    random_list = [random.randint(1, list_size) for _ in range(list_size)]

    functions = [double_loop, calc_min, store_min]
    results = []

    for function in functions:
        start = time.perf_counter_ns()
        results.append(function(random_list))
        end = time.perf_counter_ns()

        print(f"  elapsed time: {(end - start) / 1000000:.3f} ms")

    print(f"Results = {results}")
