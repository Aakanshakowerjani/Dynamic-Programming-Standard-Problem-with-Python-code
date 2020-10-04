import sys


def MCM(array, start, end):
    min_ele = sys.maxsize
    if start >= end:
        return 0
    for k in range(start, end ):
        temp = (
            MCM(array, start, k)
            + MCM(array, k + 1, end)
            + array[start - 1] * array[k] * array[end]
        )
        min_ele = min(temp, min_ele)
    return min_ele


def main():
    array = list(map(int, input("enter array").split()))
    start = 1
    end = len(array) - 1
    print(MCM(array, start, end))


if __name__ == "__main__":
    main()
