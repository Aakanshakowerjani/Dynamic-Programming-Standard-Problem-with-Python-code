length1 = int(input("enter length of string 1"))
length2 = int(input("enter length of string 2"))
dp = [[-1 for i in range(length1 + 1)] for j in range(length2 + 1)]


def longestCommonSubstring(string1, string2, length1, length2, max_ele):
    if length1 == 0 or length2 == 0:
        return 0

    elif dp[length2][length1] != -1:
        return dp[length2][length1]

    elif string1[length1 - 1] == string2[length2 - 1]:
        dp[length2][length1] = 1 + longestCommonSubstring(
            string1, string2, length1 - 1, length2 - 1,max_ele
        )
        if dp[length2][length1] > max_ele:
            max_ele = dp[length2][length1]
        return dp[length2][length1]

    else:
        dp[length2][length1] = 0
        return dp[length2][length1]


def main():
    string1 = input("enter string 1\n")
    string2 = input("enter sting 2\n")

    string1 = [i for i in string1]
    string2 = [i for i in string2]
    max_ele = 0

    print(longestCommonSubstring(string1, string2, length1, length2, max_ele))
    print(max_ele)

if __name__ == "__main__":
    main()
