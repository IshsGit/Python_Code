def edit_distance(str1, str2):
    # Initialize a 2D table to store edit distances
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill in the base cases
    for i in range(m + 1):
        dp[i][0] = i  # Number of deletions to match str1[:i] to empty string
    for j in range(n + 1):
        dp[0][j] = j  # Number of insertions to match empty string to str2[:j]

    # Fill in the rest of the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                # Characters match, no operation needed
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,  # Deletion
                               dp[i][j - 1] + 1,  # Insertion
                               dp[i - 1][j - 1] + 1)  # Substitution

    # The bottom-right corner of the table contains the edit distance
    return dp[m][n]
