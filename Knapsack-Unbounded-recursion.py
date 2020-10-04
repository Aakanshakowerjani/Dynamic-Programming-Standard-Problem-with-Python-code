def Knapsack(weight_array, value_array, bag_weight, size):
    if bag_weight == 0 or size == 0:
        return 0
    elif weight_array[size - 1] <= bag_weight:
        return max(
            value_array[size - 1]
            + Knapsack(
                weight_array, value_array, bag_weight - weight_array[size - 1], size
            ),
            Knapsack(weight_array, value_array, bag_weight, size - 1),
        )
    else:
        return Knapsack(weight_array, value_array, bag_weight, size - 1)


def main():
    bag_weight = int(input("enter desired weight"))
    size = int(input("enter no of item"))
    weight_array = list(
        map(int, input("enter weight array separated by space").split())
    )
    value_array = list(map(int, input("enter value array separated by space").split()))
    print(Knapsack(weight_array, value_array, bag_weight, size))


if __name__ == "__main__":
    main()
