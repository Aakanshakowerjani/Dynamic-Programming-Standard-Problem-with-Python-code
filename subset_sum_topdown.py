sum1 = int(input("enter sum required"))
size = int(input("enter size of array"))
dp = [[0 for i in range(sum1 + 1)] for j in range(size + 1)]


def subset_sum(array, sum, size):
    for element in range(size + 1):
        for sub_sum in range(sum + 1):
            if sub_sum == 0:
                dp[element][sub_sum] = True
            elif element == 0 and sub_sum != 0:
                dp[element][sub_sum] = False
            elif array[element - 1] <= sub_sum:
                dp[element][sub_sum] = (
                    dp[element - 1][sub_sum - array[element - 1]]
                    or dp[element - 1][sub_sum]
                )
            else:
                dp[element][sub_sum] = dp[element - 1][sub_sum]

    print(dp[size])

    return dp[size][sum]


def main():
    array = list(map(int, input("enter elements of array separated by space").split()))
    print(subset_sum(array, sum1, size))


if __name__ == "__main__":
    main()
