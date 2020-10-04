def longestPalindromicSubseq(string, length, new_string):
    dp = [[-1 for i in range(length + 1)] for j in range(length + 1)]

    for len1 in range(length + 1):
        for new_len in range(length + 1):
            if len1 == 0 or new_len == 0:
                dp[len1][new_len] = 0
            elif string[len1 - 1] == new_string[new_len - 1]:
                dp[len1][new_len] = 1 + dp[len1 - 1][new_len - 1]
            else:
                dp[len1][new_len] = max(dp[len1 - 1][new_len], dp[len1][new_len - 1])
    return dp[length][length], dp


def printLongestPalindromicSubSeq(string, length):
    new_string = string[::-1]
    palindromic_length, dp = longestPalindromicSubseq(string, length, new_string)
    palindromic_subseq = ""
    new_length = length
    while length > 0 and new_length > 0:
        if string[length - 1] == new_string[new_length - 1]:
            palindromic_subseq += string[length - 1]
            length -= 1
            new_length -= 1
        elif dp[length][new_length - 1] > dp[length - 1][new_length]:
            new_length -= 1
        else:
            length -= 1
    return palindromic_subseq, palindromic_length


def main():
    length = int(input("enter the length of string\n"))
    string = input("enter string\n")
    pal_subseq, pal_len = printLongestPalindromicSubSeq(string, length)
    print("Longest palindromic subsequence is ", pal_len, "->", pal_subseq)


if __name__ == "__main__":
    main()
