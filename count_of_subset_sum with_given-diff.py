diff=int(input('enter required difference'))
size = int(input("enter the no of elements"))
array = list(map(int, input("enter the arrays element saparated by space").split()))
sum1=(diff+sum(array))//2
dp = [[-1 for i in range(sum1 + 1)] for j in range(size + 1)]


def count_of_subset_sum(array, sum, size):
    for element in range(size + 1):
        for sub_sum in range(sum + 1):
            if sub_sum == 0:
                dp[element][sub_sum] = 1
            elif element == 0 and sub_sum != 0:
                dp[element][sub_sum] = 0
            elif array[element - 1] <= sub_sum:
                dp[element][sub_sum] = (
                    dp[element - 1][sub_sum - array[element - 1]]
                    + dp[element - 1][sub_sum]
                )
            else:
                dp[element][sub_sum] = dp[element - 1][sub_sum]
    return dp[size][sum]


def main():
    count = count_of_subset_sum(array, sum1, size)
    print(count)


if __name__ == "__main__":
    main()
