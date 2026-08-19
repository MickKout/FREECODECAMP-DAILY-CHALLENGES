def exact_change(amount):
    coins = [1, 5, 10, 25]
    ways = [0] * (amount + 1)
    ways[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            ways[i] += ways[i - coin]

    return ways[amount]