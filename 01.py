import timeit

coins = [50, 25, 10, 5, 2, 1]

# Жадібний алгоритм
def find_coins_greedy(amount):
    result = {}
    
    for coin in coins:
        while amount >= coin:
            if coin in result:
                result[coin] += 1
            else:
                result[coin] = 1
            amount -= coin
            
    #print(f"Greedy result: {result}")      
    return result

# Динамічне програмування
def find_min_coins(amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)
    
    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_used[x] = coin
    
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    
    #print(f"Dynamic programming result: {result}")
    return result

# Вимірювання часу виконання обох алгоритмів
def measure_time_with_timeit(func, amount):
    timer = timeit.Timer(lambda: func(amount))
    return timer.timeit(number=100)  # Запустити 100 разів для кращої точності

def evaluate_algorithms(max_amount):
    results = []
    for amount in range(1, max_amount + 1):
        greedy_time = measure_time_with_timeit(find_coins_greedy, amount)
        dp_time = measure_time_with_timeit(find_min_coins, amount)
        results.append((amount, greedy_time, dp_time))
    
    return results

# Тестування:
max_amount = 113
results = evaluate_algorithms(max_amount)

# Вивести результати
for amount, greedy_time, dp_time in results:
    print(f"Amount: {amount}, Greedy Time: {greedy_time:.5f}s, Dynamic programming Time: {dp_time:.5f}s")
