import math
import convert


class MyTwoSumR:
    def twoSum(nums, target):
        # Create a dictionary to store the indices of visited numbers
        indices = {}

        # Iterate through the list
        # Calculate the complement needed to reach the target
        # Check if the complement is in the dictionary
        # If yes, return the indices
        # If not, add the current number and its index to the dictionary
        for i in range(len(nums)):
            comp = target-nums[i]
            if comp in indices:
                return [indices[comp], i]
            indices[nums[i]] = i


# Technique/Algorithm: Hash Table
# Example:
# nums = [2, 7, 11, 15]
# target = 9
# print(twoSum(nums, target))
# Output: [0, 1]

class MyRevR:
    def reverseString(self, s):
        # Initialize two pointers, left and right
        # Iterate until left is less than right
        # Swap characters at the left and right pointers
        # Move left pointer to the right
        # Move right pointer to the left
        print(s[::-1])


# Technique/Algorithm: Two-Pointers
# Example:
# c1 = MyRevR()
# c1.reverseString("hello")

# Output: "olleh"

# # Example usage:
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = head.next

# # Check for a cycle
# print(ListSol.hasCycle(head))

class MyLongSub:
    def lengthOfLongestSubstring(s):
        # Create a dictionary to store the indices of characters
        # Initialize two pointers, left and right
        # Initialize the maximum length variable
        # Iterate through the string using the right pointer
        # If the character is in the dictionary and its index is greater than or equal to the left pointer
        # Update the left pointer to the next index of the repeating character
        # Update the dictionary with the current character and its index
        # Update the maximum length if needed
        indices = {}
        left = right = 0
        maximum_length = 1
        for idx, right in enumerate(s):
            if right in indices and idx >= left:
                left = indices[right]+1
            indices[right] = idx
            maximum_length = max(maximum_length, idx-left+1)
        return maximum_length


class MyisValid():
    def isValid(self, s) -> str:
        # Create a stack to keep track of open parentheses
        # Iterate through the string
        # If it's an open parenthesis, push it onto the stack
        # If it's a closing parenthesis, check if the stack is empty
        # If empty, return False
        # If not, pop the top element from the stack and check if it matches the current closing parenthesis
        # If not, return False
        # Check if the stack is empty at the end
        s = list(s)
        open_stack = []
        parens = {"(": ")", "{": "}", "[": "]"}
        for p in s:
            if p in ["(", "[", "{"]:
                open_stack.append(p)
            else:
                if not open_stack:
                    return False
                if parens.get(open_stack.pop()) != p:
                    return False
        return not open_stack


# Technique/Algorithm: Stack
# Example:
# c1 = MyisValid()
# print(c1.isValid("()[]{}"))
# Output: True
"""
Problem: Compute the Sum of Squares
Sample Input: n = 3
Sample Output: 14 (Explanation: 1^2 + 2^2 + 3^2 = 14)
"""


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
lass MyString:
    def strComp(self, s):
        count = 0
        compressed = ""
        checkChar = s[0]
        for c in s:
            if c != checkChar:
                compressed += checkChar+str(count)
                count = 0
            count += 1
            checkChar = c
        compressed += checkChar+str(count)
        print("compressed: ", compressed)


# c1 = MyString()
# c1.strComp("aabcccccaaa")

"""
taking two sorted lists as input and merging them into a single sorted list. The input lists are assumed 
to be already sorted in ascending order, and the goal is to combine them in such a way that the resulting list is also sorted.
Problem: Merge Sorted Lists
Sample Input: [1, 3, 5], [2, 4, 6]
Sample Output: [1, 2, 3, 4, 5, 6]
"""
# extend list1 with list2 and sort it then return it