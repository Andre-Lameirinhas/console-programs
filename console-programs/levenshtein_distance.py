import argparse
from time import perf_counter
from functools import lru_cache


@lru_cache(maxsize=4095)
def levenshtein_distance(initial_word: str, final_word: str):

    if not initial_word and not final_word:
        # end of the line
        return 0

    if not initial_word:
        # insert all remaining letters
        print(f"insert {final_word}")
        return len(final_word)

    if not final_word:
        # delete all remaining letters
        print(f"delete {initial_word}")
        return len(initial_word)

    if initial_word[0] == final_word[0]:
        # no operation as letters are the same
        print(f"noop on {initial_word} and {final_word}")
        return levenshtein_distance(initial_word[1:], final_word[1:])

    dist, method = min(
        # substitution
        (levenshtein_distance(initial_word[1:], final_word[1:]), "sub"),
        # insertion
        (levenshtein_distance(initial_word, final_word[1:]), "ins"),
        # deletion
        (levenshtein_distance(initial_word[1:], final_word), "del"),
    )
    print(initial_word,final_word,dist,method)
    return dist + 1


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Levenshtein Distance")
    parser.add_argument("initial_word", type=str, help="Initial word")
    parser.add_argument("final_word", type=str, help="Final word")
    args = parser.parse_args()

    start = perf_counter()
    distance = levenshtein_distance(args.initial_word, args.final_word)
    end = perf_counter()

    print(f"Levenshtein distance = {distance}")
    print(f"took {(end - start)*1000:.3f} ms")
