from test_framework import generic_test


def buy_and_sell_stock_twice(prices):
    max_total_profit, min_price_so_far = 0.0, float('inf')
    first_buy_sell_profit = [0] * len(prices)
    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        max_total_profit = max(max_total_profit, price - min_price_so_far)
        first_buy_sell_profit[i] = max_total_profit

    max_price_so_far = float('-inf')
    second_buy_sell_profit = [0] * len(prices)
    second_max_profit = 0.0
    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_price_so_far = max(max_price_so_far, price)
        second_max_profit = max(second_max_profit, max_price_so_far - price)
        second_buy_sell_profit[i] = second_max_profit

    total_profit = []
    for i in range(len(prices)):
        total_profit.append(first_buy_sell_profit[i]  + second_buy_sell_profit[i])

    return max(total_profit)



# xs = [12, 11, 13, 9, 12, 8, 14, 13, 15]
# print(F"buy_and_sell_stock_twice(xs) = {buy_and_sell_stock_twice(xs)}")



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
