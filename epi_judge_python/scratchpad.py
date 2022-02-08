def sol(n: int) -> ((int)):
    def non_attacking(cell: int, previous_rows: (int)) -> bool:
        if cell in previous_rows:
            return False

        previous_row_col_tuple = [(x, y) for x, y in enumerate(previous_rows)]

        x, y = len(previous_rows), cell
        diagnol = []
        while x > 0 and y > 0:
            x, y = x - 1, y - 1
            diagnol.append((x, y))

        if set(previous_row_col_tuple).intersection(diagnol):
            return False

        x, y = len(previous_rows), cell
        diagnol = []
        while x > 0 and y < n - 1:
            x, y = x - 1, y + 1
            diagnol.append((x, y))

        if set(previous_row_col_tuple).intersection(diagnol):
            return False

        return True

    def f(partial_result):
        if len(partial_result) >= n: # we found a solution
            result.append(partial_result[:])
            return

        for i in range(n):
            if non_attacking(i, partial_result):
                f(partial_result + [i])

    result = []
    partial_result = []
    for col in range(n):
        partial_result.append(col)
        f(partial_result)
        partial_result.clear()
    return result


n = 4
output = sol(4)
print(output)