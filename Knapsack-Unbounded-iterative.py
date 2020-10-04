def knapsack(weight_array, value_array, bag_weight, size):

    dp = [[-1 for i in range(bag_weight + 1)] for j in range(size + 1)]

    for item in range(size + 1):
        for weight in range(bag_weight + 1):
            if item == 0 or weight == 0:
                dp[item][weight] = 0
            elif weight_array[item - 1] <= weight:
                dp[item][weight] = max(
                    value_array[item - 1] + dp[item][weight - weight_array[item - 1]],
                    dp[item - 1][weight],
                )
            else:
                dp[item][weight] = dp[item - 1][weight]

    return dp[size][bag_weight]


def main():
    bag_weight = int(input("enter weight of bag"))
    size = int(input("enter no of items"))
    weight_array = list(map(int, input("enter weight separated by space").split()))
    value_array = list(map(int, input("enter value separated by space").split()))
    print(knapsack(weight_array, value_array, bag_weight, size))


if __name__ == "__main__":
    main()
