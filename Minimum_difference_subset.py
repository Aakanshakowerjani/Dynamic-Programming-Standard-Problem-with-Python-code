def minimum_difference_subset(array, sum, size):
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

    new_list = dp[size]
    min_element = sum
    for i in range(len(new_list) // 2):
        if new_list[i]==True:
            min_element = min(min_element, sum - (2 * i))
    return min_element


def main():
    size = int(input("enter size of array"))
    array = list(map(int, input("enter arrays element separated by space").split()))
    sum1 = sum(array)
    min_diff = minimum_difference_subset(array, sum1, size)
    print(min_diff)


if __name__ == "__main__":
    main()
