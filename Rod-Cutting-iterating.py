def rodCutting(length_array, value_array, length, size):
    dp = [[-1 for i in range(length + 1)] for j in range(size + 1)]

    for item in range(size + 1):
        for sub_length in range(length + 1):
            if item == 0 or sub_length == 0:
                dp[item][sub_length] = 0
            elif length_array[item - 1] <= sub_length:
                dp[item][sub_length] = max(
                    value_array[item - 1]
                    + dp[item][sub_length - length_array[item - 1]],
                    dp[item - 1][sub_length],
                )
            else:
                dp[item][sub_length] = dp[item - 1][sub_length]

    return dp[size][length]


def main():
    length = int(input("enter the length of rod"))
    size = length
    value_array = list(map(int, input("enter the values separated by space").split()))
    length_array = [i for i in range(1, length + 1)]
    print(rodCutting(length_array, value_array, length, size))


if __name__ == "__main__":
    main()
