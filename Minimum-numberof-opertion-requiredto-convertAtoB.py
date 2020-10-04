def longestCommonSubsequence(stringA, stringB, lengthA, lengthB):
    dp = [[-1 for i in range(lengthB + 1)] for j in range(lengthA + 1)]
    for lenA in range(lengthA + 1):
        for lenB in range(lengthB + 1):
            if lenA == 0 or lenB == 0:
                dp[lenA][lenB] = 0
            elif stringA[lenA - 1] == stringB[lenB - 1]:
                dp[lenA][lenB] = 1 + dp[lenA - 1][lenB - 1]
            else:
                dp[lenA][lenB] = max(dp[lenA - 1][lenB], dp[lenA][lenB - 1])
    return dp[lengthA][lengthB]


def minimumNoOfOperation(stringA, stringB, lengthA, lengthB):
    lcs_length = longestCommonSubsequence(stringA, stringB, lengthA, lengthB)
    insertion_req = lengthB - lcs_length
    deletion_req = lengthA - lcs_length
    min_operation = insertion_req + deletion_req
    return deletion_req, insertion_req, min_operation


def main():
    lengthA = int(input("enter length of A"))
    lengthB = int(input("enter length of B"))
    stringA = input("enter string A")
    stringB = input("enter string B")

    deletion_req, insertion_req, min_operation = minimumNoOfOperation(
        stringA, stringB, lengthA, lengthB
    )
    print(
        "Minimum no of deletion required to convert string A to String B is : ",
        deletion_req,
    )
    print(
        "Minimum no of insertion required to convert string A to String B is : ",
        insertion_req,
    )
    print(
        "Minimum no of operation required to convert string A to String B is : ",
        min_operation,
    )


if __name__ == "__main__":
    main()
