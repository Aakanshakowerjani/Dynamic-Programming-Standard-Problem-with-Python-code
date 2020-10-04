def longestRepeatingSubseq(string, length, new_string):
    dp = [[-1 for i in range(length + 1)] for j in range(length + 1)]
    for len1 in range(length + 1):
        for len2 in range(length + 1):
            if len1 == 0 or len2 == 0:
                dp[len1][len2] = 0
            elif string[len1 - 1] == new_string[len2 - 1] and len1 != len2:
                dp[len1][len2] = 1 + dp[len1 - 1][len2 - 1]
            else:
                dp[len1][len2] = max(dp[len1 - 1][len2], dp[len1][len2 - 1])
    return dp[length][length], dp


def printLongestRepeatingSubseq(string, length):
    new_string = string
    new_length = length
    repeative_seq = ""
    rep_seq_len, dp = longestRepeatingSubseq(string, length, new_string)
    while length > 0 and new_length > 0:
        if string[length - 1] == new_string[new_length - 1] and length != new_length:
            repeative_seq += string[length - 1]
            length -= 1
            new_length -= 1
        elif dp[length - 1][new_length] > dp[length][new_length - 1]:
            length -= 1
        else:
            new_length -= 1
    return repeative_seq, rep_seq_len


def main():
    length = int(input("enter the length of string"))
    string = input("enter the string")
    repeative_seq, rep_seq_len = printLongestRepeatingSubseq(string, length)
    print("Longest Repeative Subsequence is ", rep_seq_len, "->", repeative_seq)


if __name__ == "__main__":
    main()
