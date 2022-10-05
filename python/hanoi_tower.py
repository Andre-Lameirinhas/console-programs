import argparse
import os
from sys import stdout
import time

class Hanoi:

    def __init__(self, n_discs, print_moves, visual):
        self.n_discs = n_discs
        self.print_moves = print_moves
        self.visual = visual
        self.moves = 0
        self.rod_a = [i for i in range(n_discs, 0, -1)]
        self.rod_b = []
        self.rod_c = []

    def _move(self, rod_from, rod_to):
        if rod_from and not rod_to or rod_from[-1] < rod_to[-1]:
            rod_to.append(rod_from.pop())
            self.moves += 1
            self._print_rods()
            self._print_state()
        else:
            print("Invalid move attempted")
            exit()

    def _step(self, n_discs, rod_from, rod_helper, rod_to):
        if n_discs != 0:
            self._step(n_discs - 1, rod_from, rod_to, rod_helper)
            self._move(rod_from, rod_to)
            self._step(n_discs - 1, rod_helper, rod_from, rod_to)

    def solve(self):
        self._print_rods()
        self._print_state()
        start = time.perf_counter_ns()
        self._step(self.n_discs, self.rod_a, self.rod_b, self.rod_c)
        end = time.perf_counter_ns()
        print(f"moves required: {self.moves}")
        print(f"elapsed time: {(end - start) / 1000000} ms")

    def _print_state(self):
        if self.print_moves:
            print("##########")
            print(f"Move: {self.moves}")
            print(f"A: {self.rod_a}")
            print(f"B: {self.rod_b}")
            print(f"C: {self.rod_c}")

    def _print_rod(self, rod):
        print_array = [""] * (self.n_discs + 1)

        print_array[0] = "=" * (2 * self.n_discs + 1) + " "
        for i in range(self.n_discs):
            line = " " * (2 * self.n_discs + 1)
            if len(rod) > i:
                line = " " * (self.n_discs - rod[i] + 1)
                line += str(rod[i]) * (2 * rod[i] - 1)
                line += " " * (self.n_discs - rod[i] + 1)
            print_array[i + 1] = line + " "

        return print_array

    def _print_rods(self):
        if self.visual:
            p_rod_a = self._print_rod(self.rod_a)
            p_rod_b = self._print_rod(self.rod_b)
            p_rod_c = self._print_rod(self.rod_c)
            rods_array = [""] * (self.n_discs + 1)

            for i in range(self.n_discs + 1):
                rods_array[i] = p_rod_a[i] + p_rod_b[i] + p_rod_c[i]

            os.system("cls" if os.name == "nt" else "clear")
            stdout.write("\n".join(rods_array[::-1]) + "\n")
            stdout.flush()
            time.sleep(0.5)
            #print("\n".join(rods_array[::-1]))

if __name__ == "__main__":

    # Command line setup
    parser = argparse.ArgumentParser(description="Towers of Hanoi")
    parser.add_argument("n_discs", type=int, help="number of discs in the starting tower")
    parser.add_argument("-p", "--print_moves", action="store_true", help="enable move printing")
    parser.add_argument("-v", "--visual", action="store_true", help="show a visual representation of the moves")
    args = parser.parse_args()

    hanoi = Hanoi(args.n_discs, args.print_moves, args.visual)
    hanoi.solve()