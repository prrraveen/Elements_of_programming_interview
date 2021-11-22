import collections
from typing import Iterator, List

from test_framework import generic_test


# def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
#     xs = list(sequence)
#     running_max = 0
#     sunset = []
#     for i, height in enumerate(reversed(xs)):
#         if height > running_max:
#             sunset.append(len(xs) - 1 - i)
#         running_max = max(running_max, height)
#     return sunset

def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    BuildingWithHeight = collections.namedtuple('BuildingWithHeight', ('id', 'height'))

    candidates = []
    for building_idx, building_height in enumerate(sequence):
        while candidates and building_height >= candidates[-1].height:
            candidates.pop()
        candidates.append(BuildingWithHeight(building_idx, building_height))
    return [candidate.id for candidate in reversed(candidates)]

def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
