length = int(input("enter the length of rod"))
size = length
dp = [[-1 for i in range(length + 1)] for j in range(size + 1)]


def rodCutting(length_array, value_array, length, size):
    if size == 0 or length == 0:
        return 0
    elif dp[size][length] != -1:
        return dp[size][length]
    elif length_array[size - 1] <= length:
        dp[size][length] = max(
            value_array[size - 1]
            + rodCutting(
                length_array, value_array, length - length_array[size - 1], size
            ),
            rodCutting(length_array, value_array, length, size - 1),
        )
        return dp[size][length]
    else:
        dp[size][length] = rodCutting(length_array, value_array, length, size - 1)
        return dp[size][length]


def main():
    value_array = list(map(int, input("enter the values separated by space").split()))
    length_array = [i for i in range(1, length + 1)]
    print(rodCutting(length_array, value_array, length, size))


if __name__ == "__main__":
    main()
