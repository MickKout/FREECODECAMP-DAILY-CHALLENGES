"""""
Max Profit
Given an array of daily stock prices and a budget (in dollars), calculate the maximum profit you could make by buying and selling the stock over the given period.

You may only sell after you buy.
You may perform at most one buy and one sell transaction. Once you sell, you cannot buy again.
You can only buy whole shares.
Return the maximum possible profit as a string, rounded down to the nearest cent and formatted to two decimal places.
"""

def get_max_profit(prices, budget):

    if len(prices) < 2:
        return "0.00"

    max_profit = 0

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] > prices[i]:
                shares = int(budget / prices[i])
                profit = shares * (prices[j] - prices[i])
                if profit > max_profit:
                    max_profit = profit

    return f"{int(max_profit * 100) / 100:.2f}"

print(get_max_profit([5, 6], 50))                                                        # "10.00"
print(get_max_profit([8, 2, 5, 10], 20))                                                 # "80.00"
print(get_max_profit([4, 5, 3, 6], 20))                                                  # "18.00"
print(get_max_profit([54.40, 51.22, 53.99, 50.28, 53.01, 52.84], 200))                  # "8.31"
print(get_max_profit([15.38, 15.01, 14.99, 14.62, 14.28], 80))                          # "0.00"
print(get_max_profit([121.45, 126.82, 122.91, 124.65, 128.83, 128.83, 127.33], 1230.25)) # "73.80"