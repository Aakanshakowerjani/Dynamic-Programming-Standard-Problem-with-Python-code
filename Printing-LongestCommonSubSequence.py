def longestCommonSubsequence(string1, string2, length1, length2):
    dp = [[-1 for i in range(length1 + 1)] for j in range(length2 + 1)]

    for sub_length2 in range(length2 + 1):
        for sub_length1 in range(length1 + 1):
            if sub_length1 == 0 or sub_length2 == 0:
                dp[sub_length2][sub_length1] = 0

            elif string1[sub_length1 - 1] == string2[sub_length2 - 1]:
                dp[sub_length2][sub_length1] = 1 + dp[sub_length2 - 1][sub_length1 - 1]

            else:
                dp[sub_length2][sub_length1] = max(
                    dp[sub_length2 - 1][sub_length1], dp[sub_length2][sub_length1 - 1]
                )
    return dp


def findLongestCommonSubsequence(string1, string2, length1, length2):
    dp = longestCommonSubsequence(string1, string2, length1, length2)
    subsequence = ""
    while length1 > 0 and length2 > 0:
        if string1[length1 - 1] == string2[length2 - 1]:
            subsequence += string1[length1 - 1]
            length1 -= 1
            length2 -= 1
        elif dp[length2][length1 - 1] > dp[length2 - 1][length1]:
            length1 -= 1
        else:
            length2 -= 1
    return subsequence


def main():
    length1 = int(input("enter the length of string1\n"))
    length2 = int(input("enter the length of string2\n"))
    string1 = input("enter first string\n")
    string1 = [i for i in string1]
    print(string1)
    string2 = input("enter second string\n")
    string2 = [i for i in string2]
    print(string2)
    subsequence = findLongestCommonSubsequence(string1, string2, length1, length2)
    print(subsequence)


if __name__ == "__main__":
    main()
