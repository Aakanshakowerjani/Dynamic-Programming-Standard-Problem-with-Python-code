def longestCommonSubsequence(string1, string2, length1, length2):
    dp = [[-1 for i in range(length1 + 1)] for j in range(length2 + 1)]
    subseq = ""

    for sub_length2 in range(length2 + 1):
        for sub_length1 in range(length1 + 1):
            if sub_length1 == 0 or sub_length2 == 0:
                dp[sub_length2][sub_length1] = 0

            elif string1[sub_length1 - 1] == string2[sub_length2 - 1]:
                subseq += string1[sub_length1 - 1]
                dp[sub_length2][sub_length1] = 1 + dp[sub_length2 - 1][sub_length1 - 1]

            else:
                dp[sub_length2][sub_length1] = max(
                    dp[sub_length2 - 1][sub_length1], dp[sub_length2][sub_length1 - 1]
                )
    return subseq


def printSuperSequence(string1, string2, length1, length2):
    subsequence = longestCommonSubsequence(string1, string2, length1, length2)
    super_seq = ""
    item1 = 0
    item2 = 0
    for seq in subsequence:
        while string1[item1] != seq:
            super_seq += string1[item1]
            item1 += 1
        while string2[item2] != seq:
            super_seq += string2[item2]
            item2 += 1
        super_seq += seq
        item1 += 1
        item2 += 1
    while item1 < length1:
        super_seq += string1[item1]
        item1 += 1
    while item2 < length2:
        super_seq += string2[item2]
        item2 += 1
    return super_seq


def main():
    length1 = int(input("enter the length of string1\n"))
    length2 = int(input("enter the length of string2\n"))
    string1 = input("enter first string\n")
    string1 = [i for i in string1]
    print(string1)
    string2 = input("enter second string\n")
    string2 = [i for i in string2]
    print(string2)
    print(printSuperSequence(string1, string2, length1, length2))


if __name__ == "__main__":
    main()
