def longestCommonSubstring(string1, string2, length1, length2, max_ele):
    dp = [[-1 for i in range(length1 + 1)] for j in range(length2 + 1)]

    for sub_length2 in range(length2 + 1):
        for sub_length1 in range(length1 + 1):

            if sub_length1 == 0 or sub_length2 == 0:
                dp[sub_length2][sub_length1] = 0

            elif string1[sub_length1-1] == string2[sub_length2-1]:
                dp[sub_length2][sub_length1] = 1 + dp[sub_length2 - 1][sub_length1 - 1]
                if max_ele < dp[sub_length2][sub_length1]:
                    max_ele = dp[sub_length2][sub_length1]

            else:
                dp[sub_length2][sub_length1] = 0
            
    return max_ele


def main():
    length1 = int(input("enter length of string 1"))
    length2 = int(input("enter length of string 2"))
    string1 = input("enter string 1\n")
    string2 = input("enter sting 2\n")

    string1 = [i for i in string1]
    string2 = [i for i in string2]
    max_ele = 0

    print(longestCommonSubstring(string1, string2, length1, length2, max_ele))


if __name__ == "__main__":
    main()
