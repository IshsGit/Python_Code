# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not allowed.

def num_decodings(message):
    if not message:
        return 0

    n = len(message)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1 if message[0] != '0' else 0

    for i in range(2, n + 1):
        if message[i - 1] != '0':
            dp[i] += dp[i - 1]

        two_digits = int(message[i - 2:i])
        if 10 <= two_digits <= 26:
            dp[i] += dp[i - 2]

    return dp[n]


# Example usage:
encoded_message = "111"
print(num_decodings(encoded_message))  # Output: 3
