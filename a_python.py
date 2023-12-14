"""
Problem: Compute the Sum of Squares
Sample Input: n = 3
Sample Output: 14 (Explanation: 1^2 + 2^2 + 3^2 = 14)
"""


import convert
import math


class MySquares:
    def sumSquares(self, n):
        sum = 0
        for x in range(1, n+1):
            sum += x**2
        return sum


# c1 = MySquares()
# print(f"{c1.sumSquares(3)}")

"""
Problem: String Compression; write a program or function that takes a string as input 
and compresses it by replacing consecutive repeated characters with the character 
followed by the count of consecutive repetitions.
Sample Input: "aabcccccaaa"
Sample Output: "a2b1c5a3"
"""

# Approach, want to iterate over the string, concat a new string with current character when a variable count is 0,
# have a condition to count the number of times the following character is the same
# Once new character, reset count to 0 and concat the string we created with the current character
