from test_framework import generic_test, test_utils

keypad_mapping = {
    0: {'0'},
    1: {'1'},
    2: {'A', 'B', 'C'},
    3: {'D', 'E', 'F'},
    4: {'G', 'H', 'I'},
    5: {'J', 'K', 'L'},
    6: {'M', 'N', 'O'},
    7: {'P', 'Q', 'R', 'S'},
    8: {'T', 'U', 'V'},
    9: {'W', 'X', 'Y', 'Z'},

}

def phone_mnemonic(phone_number):
    def phone_mnemonic_helper(digit):
        if digit == len(phone_number):
            result.append(''.join(partial_mnemonic))
        else:
            for ch in keypad_mapping[int(phone_number[digit])]:
                partial_mnemonic[digit] = ch
                phone_mnemonic_helper(digit + 1)

    result, partial_mnemonic = [], [0] * len(phone_number)
    phone_mnemonic_helper(0)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
