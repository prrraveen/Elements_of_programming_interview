from test_framework import generic_test

def get_next_number(xs):
    result = []
    number, count = xs[0], 1
    for i in range(1, len(xs)):
        if xs[i] == number:
            count += 1
        else:
            result += [str(count), number]
            # clean up
            number = xs[i]
            count = 1
    result += [str(count), number]
    return ''.join(result)

# print(F"get_next_number(21) = {get_next_number('21')}")

def look_and_say(n: int) -> str:
    last = '1'
    for i in range(n - 1):
        last = get_next_number(last)
    return last



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))


def look_and_say(n: int) -> str:
    xs = ['1']
    for i in range(n):
        *rest, last = xs
        next_number = get_next_number(last)
        xs.append(next_number)
    return xs[n-1]



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
