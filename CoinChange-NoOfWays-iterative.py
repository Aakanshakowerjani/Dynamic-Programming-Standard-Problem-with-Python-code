def coinChange(coin_array, sum, size):

    dp = [[-1 for i in range(sum + 1)] for j in range(size + 1)]
    for coin in range(size + 1):
        for sub_sum in range(sum + 1):
            if sub_sum == 0:
                dp[coin][sub_sum] = 1
            elif sub_sum != 0 and coin == 0:
                dp[coin][sub_sum] = 0
            elif coin_array[coin - 1] <= sub_sum:
                dp[coin][sub_sum] = (
                    dp[coin][sub_sum - coin_array[coin - 1]] + dp[coin - 1][sub_sum]
                )
            else:
                dp[coin][sub_sum] = dp[coin - 1][sub_sum]

    return dp[size][sum]+1


def main():
    sum1 = int(input("enter required sum"))
    size = int(input("enter no of coins"))
    coin_array = list(map(int, input("enter coins separated by space").split()))
    print(coinChange(coin_array, sum1, size))


if __name__ == "__main__":
    main()
