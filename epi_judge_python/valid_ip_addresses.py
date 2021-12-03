from typing import List

from test_framework import generic_test

def get_valid_ip_address(s: str) -> List[str]:
    result, k  = [], 4
    def is_valid_part(s):
        return len(s) == 1 or (s[0] != '0' and int(s) <= 255)

    def get_valid_ip_address_helper(s_idx, dot_n, partial_result=[]):
        print(F"s_idx, dot_n, partial_result = {s_idx, dot_n, partial_result}")
        if s_idx > len(s) - 1: #if there are no more digits left for remaining dots
            if dot_n == k + 2:
                ip = '.'.join(partial_result)
                if ip not in result:
                    result.append(ip)
            return

        for i in range(1, min(len(s), 4)):
            chunk = s[s_idx:s_idx + i]
            if is_valid_part(chunk):
                get_valid_ip_address_helper(s_idx+i, dot_n + 1, partial_result + [chunk])

    if len(s) < k + 1 or len(s) > 3 * (k + 1):
        return result
    get_valid_ip_address_helper(0, 1)
    return result

xs = '192168111'
output = get_valid_ip_address(xs)
print(F"len(output) = {len(output)}")
for ip in output:
    print(ip)

# def _get_valid_ip_address(s: str) -> List[str]:
#     def is_valid_part(s):
#         return len(s) == 1 or (s[0] != '0' and int(s) <= 255)
#
#     result, parts = [], [None] * 4
#     for i in range(1, min(4, len(s))):
#         parts[0] = s[:i]
#         if is_valid_part(parts[0]):
#             for j in range(1, min(len(s) - i, 4)):
#                 parts[1] = s[i:i+j]
#                 if is_valid_part(parts[1]):
#                     for k in range(1, min(len(s) - i - j, 4)):
#                         parts[2], parts[3] = s[i+j: i + j + k], s[i+j+k:]
#                         if is_valid_part(parts[2]) and is_valid_part(parts[3]):
#                             result.append('.'.join(parts))
#     return result
#
#
# def comp(a, b):
#     return sorted(a) == sorted(b)
#
#
# if __name__ == '__main__':
#     exit(
#         generic_test.generic_test_main('valid_ip_addresses.py',
#                                        'valid_ip_addresses.tsv',
#                                        get_valid_ip_address,
#                                        comparator=comp))
