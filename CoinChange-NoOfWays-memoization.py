sum1 = int(input("enter the required sum"))
size = int(input("enter the size"))
dp = [[-1 for i in range(sum1 + 1)] for j in range(size + 1)]


def coinchange(coin_array, sum, size):
    if sum == 0:
        return 1
    elif sum != 0 and size == 0:
        return 0
    elif dp[size][sum] != -1:
        return dp[size][sum]

    elif coin_array[size - 1] <= sum:
        dp[size][sum] = coinchange(
            coin_array, sum - coin_array[size - 1], size
        ) + coinchange(coin_array, sum, size - 1)
        return dp[size][sum]

    else:
        dp[size][sum] = coinchange(coin_array, sum, size - 1)
        return dp[size][sum]


def main():

    coin_array = list(map(int, input("enter the coin separated by space").split()))
    print(coinchange(coin_array, sum1, size))


if __name__ == "__main__":
    main()
