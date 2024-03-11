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


class MyString:
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


class MyLists:
    def mergeList(self, list1, list2):
        list1.extend(list2)
        list1.sort()
        print(list1)


# c1 = MyLists()
# c1.mergeList([5, 4, 6], [1, 3, 2])

"""
developing a program or function that takes a string of text as input and outputs a dictionary where the keys
are unique words in the text, and the values represent the frequency of each word in the text.
Problem: Word Frequency Counter
Sample Input: "the quick brown fox jumps over the lazy dog"
Sample Output: {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
"""
# Iterate through the string, append an empty dictionary if the key doesn't exist it assigns the current element of the string as a key
# and the value is initialize to 1, if a following iteration the key exists it increments the counter by 1
# It returns the dictionary


class MyFrequency:
    def countWords(self, s):
        strArr = s.split(" ")
        dict = {}
        for char in strArr:
            if not dict.get(char):
                dict[char] = 1
            else:
                dict[char] += 1
        print(dict)


# c1 = MyFrequency()
# c1.countWords("the quick brown fox jumps over the lazy dog")

"""
If-Else, While Loops, For Loops:
Problem: Palindrome Check
determining whether a given input string is a palindrome or not. A palindrome is a sequence of characters 
that reads the same forwards as backward, ignoring spaces, punctuation, and capitalization.
Sample Input: "radar"
Sample Output: True
"""


class MyPalindrome:
    def isPalindrome(self, word):
        rev = ""
        for char in word[::-1]:
            rev += char
        print("rev: ", rev)
        if rev == word:
            print("Is palindrome")
        else:
            print("not palindrome")


# c1 = MyPalindrome()
# c1.isPalindrome("radar")

"""
Functions, Lambda:
Problem: High-Order Function
 involves the application of a given function to a range of input values, producing a list of corresponding output values.
A high-order function typically takes another function as an argument or returns a function as its result.
Sample Input: f(x) = x^2, range [1, 3]
Sample Output: [1, 4, 9]
"""


class MyHigh:
    def squareAll(self, fcn, input_range):
        outputList = []
        for x in range(input_range[0], input_range[-1]+1):
            outputList.append(fcn(x))
        print(outputList)


# c1 = MyHigh()
# c1.squareAll(lambda a: a**2, [1, 3])

"""
Problem: Geometry Classes
involves creating classes for basic geometric shapes, such as a circle and a rectangle.
 Each class should have methods to calculate the area and perimeter of the shape based 
 on its specific attributes. The problem provides sample input involving instances of 
 the Circle and Rectangle classes, and the desired output includes the calculated area and perimeter for each shape.
Sample Input: Circle(radius=5), Rectangle(length=4, width=3)
Sample Output: Area: 78.54, Perimeter: 31.42 (for Circle), Area: 12, Perimeter: 14 (for Rectangle)
"""


class Shapes:
    def __init__(self, l, w, r):
        self.l = l
        self.w = w
        self.r = r


class Circle(Shapes):
    def __init__(self, r):
        super().__init__(None, None, r)

    def area(self):
        print(float(math.pi*(self.r**2)))

    def perimeter(self):
        print(float(2*math.pi*self.r))


class Rectangle(Shapes):

    def __init__(self, l, w):
        super().__init__(l, w, None)

    def area(self):
        print(float(self.l*self.w))

    def perimeter(self):
        print(float(2*(self.l+self.w)))


# c1 = Shapes(4, 3, 5)
# c2 = Circle(5)
# c2.area()
# c2.perimeter()
# c3 = Rectangle(4, 3)
# c3.area()
# c3.perimeter()
# iterate through list from start to end point.


class MyMin:
    def minSub(self, l1, target):
        start = end = curr_sum = 0
        min_length = float('inf')
        for end in range(len(l1)):
            curr_sum += l1[end]
            end += 1
            while curr_sum >= target:
                min_length = min(min_length, end-start)
                curr_sum -= l1[start]
                start += 1
        if min_length == float('inf'):
            print("no indices")
        else:
            print(min_length)


# c1 = MyMin()
# c1.minSub([2, 3, 1, 2, 4, 3], 7)

"""
- **Problem: Shortest Unsorted Continuous Subarray**
  - **Sample Input:** `[2, 6, 4, 8, 10, 9, 15]`
  - **Sample Output:** `[2, 4, 6, 8, 9, 10, 15]` (Explanation: The subarray [6, 4, 8, 10, 9] is unsorted)
"""


class Solution:
    def findUnsortedSubarray(self, nums):
        temp = sorted(nums)
        if temp[:] == nums[:]:
            return 0
        l, r = 0, len(nums)-1
        for i, x in enumerate(nums):
            if temp[i] != x:
                l = i
                break
        while temp[r] == nums[r]:
            r -= 1
        return r-l+1


# c1 = Solution()
# (c1.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))


"""
- **Problem: Shortest Unsorted Continuous Subarray**
  - **Sample Input:** `[2, 6, 4, 8, 10, 9, 15]`
  - **Sample Output:** `[2, 4, 6, 8, 9, 10, 15]` (Explanation: The subarray [6, 4, 8, 10, 9] is unsorted)
"""


class MySortArr:
    def findSub(self, l1):
        sorted_list = sorted(l1)
        start = 0
        end = len(l1)-1
        while start < len(l1) and l1[start] == sorted_list[start]:
            start += 1
        while end > start and l1[end] == sorted_list[end]:
            end -= 1
        sub_length = end-start+1 if start < end else 0
        print(sub_length)


# Example usage:
# c1 = MySortArr()
# result = c1.findSub([2, 6, 4, 8, 10, 9, 15])

"""
- **Problem: Longest Consecutive Increasing Sequence**
  - **Sample Input:** `[100, 4, 200, 1, 3, 2]`
  - **Sample Output:** `4` (Explanation: The longest consecutive increasing sequence is [1, 2, 3, 4])
"""


class MyAnagramR:
    def findAnagrams(self, s: str, p: str) -> list:
        # have 2 strings, in order check if s contains p
        # store the starting index
        if len(s) == 0:
            print(0)
        p_freq = {}
        s_freq = {}
        indices = []

        for char in p:
            p_freq[char] = p_freq.get(char, 0)+1
        for i in range(len(s)-len(p)+1):

            for char in s[i:i+len(p)]:
                s_freq[char] = s_freq.get(char, 0)+1
            print("p_freq: ", p_freq)
            print("s_freq: ", s_freq)

            if p_freq == s_freq:
                print("i: ", i)
                indices.append(i)
            s_freq = {}
        print(indices)


# c1 = MyAnagramR()
# c1.findAnagrams("cbaebabacd", "abc")

"""
Problem 1: Two Sum
Description: Given an array of integers nums and an integer target, 
return the indices of the two numbers such that they add up to target.
"""


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
