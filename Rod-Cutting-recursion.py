def rodCutting(length_array, value_array, length, size):
    if size == 0 or length == 0:
        return 0
    elif length_array[size - 1] <= length:
        return max(
            value_array[size - 1]
            + rodCutting(
                length_array, value_array, length - length_array[size - 1], size
            ),
            rodCutting(length_array, value_array, length, size - 1),
        )
    else:
        return rodCutting(length_array, value_array, length, size - 1)


def main():
    length = int(input("enter length of rod"))
    value_array = list(map(int, input("enter value separated by space").split()))
    length_array = [i for i in range(1, length + 1)]
    size = length
    print(rodCutting(length_array, value_array, length, size))


if __name__ == "__main__":
    main()
