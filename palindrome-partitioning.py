import sys

size = int(input("enter the size of array"))
dp = [[-1 for i in range(size + 1)] for j in range(size + 1)]


def palindromePartitioning(array, start, end):
    if start > end:
        return 0
    if dp[start][end] != -1:
        return dp[start][end]
    min_ele = sys.maxsize
    for element in range(start, end):
        temp = (
            palindromePartitioning(array, start, element)
            + palindromePartitioning(array, element + 1, end)
            + 1
        )
        min_ele = min(temp, min_ele)
    dp[start][end] = min_ele

    return dp[start][end]


def main():
    input1 = input("enter string")
    array = [i for i in input1]
    print(palindromePartitioning(array, 0, size - 1))


if __name__ == "__main__":
    main()
