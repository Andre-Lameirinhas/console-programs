import argparse
import matplotlib.pyplot as plt
import sys
import time

class Fibonacci:

    def __init__(self, number, dynamic, graph):
        self.number = number
        self.dynamic = dynamic
        self.graph = graph
        self.f_calls = 0
        self.values = list()

    def calculate(self):
        if self.graph:
            lin_vals = list()
            exp_vals = list()

            start = time.perf_counter_ns()
            for i in range(self.number + 1):
                self.values = [0 for i in range(self.number + 1)]
                step_start = time.perf_counter_ns()
                self._lin_fib(i)
                step_end = time.perf_counter_ns()
                lin_vals.append((step_end - step_start) / 1000000)

                step_start = time.perf_counter_ns()
                self._exp_fib(i)
                step_end = time.perf_counter_ns()
                exp_vals.append((step_end - step_start) / 1000000)
            end = time.perf_counter_ns()

            print(f"elapsed time: {(end - start) / 1000000} ms")

            plt.plot(lin_vals, "bo", label="dynamic approach")
            plt.plot(exp_vals, "ro", label="non-dynamic approach")
            plt.xlabel("sequence index")
            plt.ylabel("duration (ms)")
            plt.title("Fibonacci Sequence Comparison")
            plt.legend()
            plt.show()

        else:
            if self.dynamic:
                self.values = [0 for i in range(self.number + 1)]

                start = time.perf_counter_ns()
                value = self._lin_fib(self.number)
                end = time.perf_counter_ns()

            else:
                start = time.perf_counter_ns()
                value = self._exp_fib(self.number)
                end = time.perf_counter_ns()

            print(f"fib[{self.number}] = {value}")
            print(f"function calls: {self.f_calls}")
            print(f"elapsed time: {(end - start) / 1000000} ms")

    # O(n) time complexity
    def _lin_fib(self, n):
        self.f_calls += 1

        if n < 2:
            return n
        if not self.values[n]:
            self.values[n] = self._lin_fib(n - 1) + self._lin_fib(n - 2)
        return self.values[n]

    # O(2^n) time complexity
    def _exp_fib(self, n):
        self.f_calls += 1

        if n < 2:
            return n
        return self._exp_fib(n - 1) + self._exp_fib(n - 2)

if __name__ == "__main__":

    # Raise recursion limit
    sys.setrecursionlimit(7000)

    # Command line setup
    parser = argparse.ArgumentParser(description="Fibonacci Sequence")
    parser.add_argument("number", type=int, help="position in the sequence to determine")
    parser.add_argument("-d", "--dynamic", action="store_true", help="enable dynamic resolution")
    parser.add_argument("-g", "--graph", action="store_true", help="create a comparison graph")
    args = parser.parse_args()

    fib = Fibonacci(args.number, args.dynamic, args.graph)
    fib.calculate()