no_of_items = int(input("enter no of items"))
bag_weight = int(input("enter bag weight"))
dp = [[0 for y in range(bag_weight + 1)] for x in range(no_of_items + 1)]


def knapsack(weight_array, value_array, bag_weight, no_of_items):

    for item in range(no_of_items + 1):
        for weight in range(bag_weight + 1):
            if item == 0 or weight == 0:
                dp[item][weight] = 0
            elif weight_array[item - 1] <= weight:
                dp[item][weight] = max(
                    value_array[item - 1]
                    + dp[item - 1][weight - weight_array[item - 1]],
                    dp[item][weight]
                )
            else:
                dp[item][weight] = dp[item - 1][weight]
    return dp[no_of_items][bag_weight]


def main():

    weight_array = list(
        map(int, input("enter weight of items separated by space").split())
    )
    value_array = list(
        map(int, input("enter value of items separated by space").split())
    )
    profit = knapsack(weight_array, value_array, bag_weight, no_of_items)
    print(profit)


if __name__ == "__main__":
    main()
