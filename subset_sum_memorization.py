sum1 = int(input("enter the required sum"))
size = int(input("enter the size of array"))
dp = [[0 for i in range(sum1 + 1)] for j in range(size + 1)]


def subset_sum(array, sum, size):
    if sum == 0:
        return True
    elif size == 0 and sum != 0:
        return False
    if dp[size][sum] != 0:
        return dp[size][sum]
    elif array[size - 1] <= sum:
        dp[size][sum] = subset_sum(
            array, sum - array[size - 1], size - 1
        ) or subset_sum(array, sum, size - 1)
        return dp[size][sum]
    else:
        dp[size][sum] = subset_sum(array, sum, size - 1)
        return dp[size][sum]


def main():
    array = list(map(int, input("enter arrays element separated by space").split()))
    print(subset_sum(array, sum1, size))


if __name__ == "__main__":
    main()
