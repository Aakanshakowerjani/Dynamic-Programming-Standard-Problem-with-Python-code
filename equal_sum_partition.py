# checking whether subset sum is possible or not

def subset_sum(array, sum, size):
    dp = [[0 for i in range(sum + 1)] for j in range(size + 1)]
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

    return dp[size][sum]


def equal_sum_partition(array, sum, size):
    if sum % 2 != 0:
        return False
    else:
        return subset_sum(array, sum // 2, size)


def main():
    size = int(input("enter the size of array"))
    array = list(map(int, input("enter element of array separated by space").split()))
    sum1=sum(array)
    print(equal_sum_partition(array, sum1, size))


if __name__ == "__main__":
    main()
