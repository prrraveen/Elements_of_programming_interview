import math
from typing import List

from test_framework import generic_test

def cap_summation(salaries, cap):
    result = 0
    for salary in salaries:
        result += min(salary, cap)
    return result


# def find_salary_cap(target_payroll: int, current_salaries: List[int]) -> float:
#     if sum(current_salaries) < target_payroll:
#         return -1.0
#     current_salaries.sort()
#     # decide the search range according to the max salary
#     left, right = 0, current_salaries[-1]
#     while not math.isclose(left, right):
#         mid = 0.5 * (left + right)
#         result = cap_summation(current_salaries, cap=mid)
#         if math.isclose(result, target_payroll):
#             print(F"mi = {mid}")
#             return mid
#         elif result < target_payroll:
#             left = mid
#         else:
#             right = mid
#     print(F"left, right = {left, right}")
#     return left

def find_salary_cap(target_payroll: int, current_salaries: List[int]) -> float:
    current_salaries.sort()
    unadjusted_salary_sum = 0.0
    for i, current_salary in enumerate(current_salaries):
        adjusted_people = len(current_salaries) - i

        adjusted_salary_sum = adjusted_people * current_salary
        if unadjusted_salary_sum + adjusted_salary_sum >= target_payroll:
            return (target_payroll - unadjusted_salary_sum) / adjusted_people
        unadjusted_salary_sum += current_salary
    return -1.0



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('find_salary_threshold.py',
                                       'find_salary_threshold.tsv',
                                       find_salary_cap))
