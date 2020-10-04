def subset_sum(array, sum, size):
    if sum == 0:
        return True
    elif size == 0 and sum != 0:
        return False
    if array[size - 1] <= sum:
        return subset_sum(array, sum - array[size - 1], size - 1) or subset_sum(
            array, sum, size - 1
        )
    else:
        return subset_sum(array, sum, size - 1)


def main():
    size = int(input("enter the size of array"))
    array = list(map(int, input("enter element of array separated by space").split()))
    sum = int(input("enter desired sum"))
    print(subset_sum(array, sum, size))


if __name__ == "__main__":
    main()
