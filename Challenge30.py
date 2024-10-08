def coin_change(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0 
    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a:
                dp[a] = min(dp[a], dp[a - coin] + 1)
    return dp[amount] if dp[amount] != amount + 1 else -1
coins = [1, 2, 5]
amount = 11
result = coin_change(coins, amount)
print(f"Minimum coins required to make {amount}: {result}")
