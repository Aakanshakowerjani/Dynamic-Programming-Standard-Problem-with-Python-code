import sys

size = int(input("enter size of array"))
dp = [[-1 for i in range(size + 1)] for j in range(size + 1)]


def mcm(array, start, end):
    min_ele = sys.maxsize
    if start >= end:
        return 0
    if dp[start][end] != -1:
        return dp[start][end]
    for element in range(start, end):
        temp = (
            mcm(array, start, element)
            + mcm(array, element + 1, end)
            + (array[start - 1] * array[element] * array[end])
        )
        if temp < min_ele:
            min_ele = temp
    dp[start][end] = min_ele
    return dp[start][end]


def main():

    array = list(map(int, input("enter sizes of array separated by space").split()))
    print("Minimum cost is", mcm(array, 1, size - 1))


if __name__ == "__main__":
    main()
