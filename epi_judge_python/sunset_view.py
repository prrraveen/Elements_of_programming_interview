import collections
from typing import Iterator, List
from test_framework import generic_test


# def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
#     if not sequence:
#         return []
#     result, max_height_so_far = [], 0
#     i = len(sequence) - 1
#     for building_height in reversed(sequence):
#         if building_height > max_height_so_far:
#             result.append(i)
#             max_height_so_far = building_height
#         i -= 1
#     return result

def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    HeightandIdx = collections.namedtuple('HeightandIdx', ('idx', 'height'))
    stack = []
    for i, building_height in enumerate(sequence):
        while stack and stack[-1].height <= building_height:
            stack.pop()
        stack.append(HeightandIdx(i, building_height))

    result = [building.idx for building in reversed(stack)]
    return result




xs = [2, 5, 3, 4, 2, 2]
expected = [1, 3, 5]




# def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
#     BuildingWithHeight = collections.namedtuple('BuildingWithHeight', ('id', 'height'))
#
#     candidates = []
#     for building_idx, building_height in enumerate(sequence):
#         while candidates and building_height >= candidates[-1].height:
#             candidates.pop()
#         candidates.append(BuildingWithHeight(building_idx, building_height))
#     return [candidate.id for candidate in reversed(candidates)]

def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
count = 1

def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
