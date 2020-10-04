def knapsack(weight_array, value_array, bag_weight, no_of_items):
    if bag_weight == 0 or no_of_items == 0:
        return 0
    elif weight_array[no_of_items - 1] <= bag_weight:
        return max(
            value_array[no_of_items - 1]
            + knapsack(
                weight_array,
                value_array,
                bag_weight - weight_array[no_of_items - 1],
                no_of_items - 1,
            ),
            knapsack(weight_array, value_array, bag_weight, no_of_items - 1),
        )

    elif weight_array[no_of_items - 1] > bag_weight:
        return knapsack(weight_array, value_array, bag_weight, no_of_items - 1)


def main():
    bag_weight = int(input("enter bag weight"))
    no_of_items = int(input("enter no items"))
    weight_array = list(map(int, input("enter weights separated by space").split()))
    value_array = list(map(int, input("enter values separated by space").split()))
    total_profit = knapsack(weight_array, value_array, bag_weight, no_of_items)
    print(total_profit)


if __name__ == "__main__":
    main()
