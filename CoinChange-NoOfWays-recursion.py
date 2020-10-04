def coinchange(coin_array, sum, size):
    if sum == 0:
        return 1
    elif sum != 0 and size == 0:
        return 0

    elif coin_array[size - 1] <= sum:
        return coinchange(coin_array, sum - coin_array[size - 1], size) + coinchange(
            coin_array, sum, size - 1
        )

    else:
        return coinchange(coin_array, sum, size - 1)


def main():
    sum1 = int(input("enter the required sum"))
    size = int(input("enter the size"))
    coin_array = list(map(int, input("enter the coin separated by space").split()))
    print(coinchange(coin_array, sum1, size))

if __name__ == "__main__":
    main()
