bag_weight = int(input("enter bag weight"))
size = int(input("enter no of items"))
dp = [[-1 for i in range(bag_weight + 1)] for j in range(size + 1)]


def knapsack(weight_array, value_array, bag_weight, size):

    if bag_weight == 0 or size == 0:
        return 0

    if dp[size][bag_weight] != -1:
        return dp[size][bag_weight]
    elif weight_array[size - 1] <= bag_weight:
        dp[size][bag_weight] = max(
            value_array[size - 1]
            + knapsack(
                weight_array, value_array, bag_weight - weight_array[size - 1], size - 1
            ),
            knapsack(weight_array, value_array, bag_weight, size - 1),
        )
        return dp[size][bag_weight]
    else:
        dp[size][bag_weight] = knapsack(weight_array, value_array, bag_weight, size - 1)
        return dp[size][bag_weight]


def main():

    weight_array = list(map(int, input("enter weights separated by space").split()))
    value_array = list(map(int, input("enter value separated by space").split()))
    profit = knapsack(weight_array, value_array, bag_weight, size)
    print(profit)


if __name__ == "__main__":
    main()
