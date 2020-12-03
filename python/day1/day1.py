from typing import List
from functools import reduce
from itertools import combinations

def load_input_text() -> List[int]:
    with open("python/day-1-input.txt") as f:
        input = f.readlines()
    input = [int(i) for i in input]
    return input


def locate_matching_group(
    value_to_match: int,
    input_list: List[int],
    number_to_match: int
    ):
    combs = combinations(input_list, number_to_match)
    for c in combs:
        if reduce(lambda a,b:a+b, c) == value_to_match:
            return c


def reduce_by_multiply(input_list: List[int]) -> int:
    return reduce(lambda a,b: a*b, matches)


if __name__ == "__main__":
    i = load_input_text()
    matches = locate_matching_group(2020, i, 3)
    answer = reduce_by_multiply(matches)
    print(answer)