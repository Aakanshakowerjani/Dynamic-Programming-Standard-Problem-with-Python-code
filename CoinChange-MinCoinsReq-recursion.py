import sys

def coinChange(coin_array, sum, size):
    if size == 0:
        return sys.maxsize - 1
    elif sum == 0 and size != 0:
        return 0
    elif size == 1:
        if sum % coin_array[0] == 0:
            return sum // coin_array[0]
        else:
            return sys.maxsize - 1
    elif coin_array[size - 1] <= sum:
        return min(
            coinChange(coin_array, sum - coin_array[size - 1], size) + 1,
            coinChange(coin_array, sum, size - 1),
        )
    else:
        return coinChange(coin_array, sum, size - 1)


def main():
    sum1 = int(input("enter the required sum"))
    size = int(input("enter no coins"))
    coin_array = list(map(int, input("enter the coins separated by space").split()))
    print(coinChange(coin_array, sum1, size))


if __name__ == "__main__":
    main()
