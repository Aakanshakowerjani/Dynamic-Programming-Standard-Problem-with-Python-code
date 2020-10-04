length1 = int(input("enter the length of string1\n"))
length2 = int(input("enter the length of string2\n"))
dp=[[-1 for i in range(length1+1)] for j in range(length2+1)]

def longestCommonSubsequence(string1, string2, length1, length2):
    if length1 == 0 or length2 == 0:
        return 0
    
    elif dp[length2][length1]!=-1:
        return dp[length2][length1]

    elif string1[length1-1] == string2[length2-1]:
        dp[length2][length1]=1 + longestCommonSubsequence(string1, string2, length1 - 1, length2 - 1)
        return dp[length2][length1]
    else:
        dp[length2][length1]= max(
            longestCommonSubsequence(string1, string2, length1 - 1, length2),
            longestCommonSubsequence(string1, string2, length1, length2 - 1),
        )
        return dp[length2][length1]


def main():
    
    string1 = input('enter first string\n')
    string1=[i for i in string1]
    print(string1)
    string2 = input('enter second string\n')
    string2=[i for i in string2]
    print(string2)
    print(longestCommonSubsequence(string1, string2, length1, length2))


if __name__ == "__main__":
    main()
