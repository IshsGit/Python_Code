"""
Problem: Temperature Converter Module
creating a module or a set of 
functions that can convert temperatures between Celsius and Fahrenheit scales. The problem
 typically defines two conversion functions: one for converting Celsius to Fahrenheit and
another for converting Fahrenheit to Celsius.
Sample Input: celsius_to_fahrenheit(0), fahrenheit_to_celsius(32)
Sample Output: 32.0°F, 0.0°C
"""

# c1 = convert.Conversion(0, 32)
# c1.cel_to_far()
# c1.far_to_cel()

"""
The "Merge Intervals" problem involves taking a collection of intervals represented as pairs of 
start and end points and merging overlapping intervals to form a new set of non-overlapping intervals.
Numbered Intervals in Arrays (New):
Problem: Merge Intervals
Sample Input: [[1,3],[2,6],[8,10],[15,18]]
Sample Output: [[1,6],[8,10],[15,18]]
"""
# If the start point of an interval is less than the endpoint of another, then
# they can be merged
# Sort the list first, then iterate through it
# We want to append a new list. The new list should have the starting point of its first interval element
# In successive iterations, we want to update the end point of that interval till it is no longer
# greater than the first element of another interval
# We want to seek the entire list before we decide to move onto the next interval in the array


class MyMerge:
    def mergeIntervals(self, our_list):

        sorted_list = sorted(our_list)
        current_interval = sorted_list[0]
        merged = [current_interval]
        for x in range(1, len(sorted_list)):
            if sorted_list[x][0] > merged[-1][1]:
                # current_interval[1] = max(sorted_list[x][1], current_interval[1])
                merged.append(sorted_list[x])
            else:
                merged[-1][1] = max(sorted_list[x][1], merged[-1][1])

        print(merged)


# c1 = MyMerge()
# c1.mergeIntervals([[1, 3], [2, 6], [8, 10], [15, 18]])

"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

"""


class MyAnagram:
    def sortAnagram(self, s1, s2):
        output_list = []
        s1Arr = list(s1)  # Splitting into individual characters
        s2Arr = list(s2)
        if len(s1Arr) > len(s2Arr):
            longest = s1Arr
            shortest = s2Arr
        else:
            longest = s2Arr
            shortest = s1Arr
        i = 0
        for x in longest:
            if x == shortest[i] and longest.index(x) not in output_list:
                output_list.append(longest.index(x))
                i += 1

        print(sorted(output_list))


# c1 = MyAnagram()
# c1.sortAnagram("cbaebabacd", "abc")

"""
Problem: Maximum Subarray Sum
Given an array of integers, find the contiguous subarray with the largest sum. The task is to determine the sum of this subarray.
For example, consider the array [-2,1,-3,4,-1,2,1,-5,4]. The contiguous subarray [4,-1,2,1] has the largest sum, which is 6. 
The goal is to devise an algorithm to efficiently compute the maximum sum of a subarray for a given array of integers.
 **Problem: Maximum Subarray Sum**
  - **Sample Input:** `[-2,1,-3,4,-1,2,1,-5,4]`
  - **Sample Output:** `6` (Explanation: The contiguous subarray [4,-1,2,1] has the largest sum)

update the problem with a problem description, do not give me the solution
"""


class MaxSubSum:
    def findSum(self, l1):
        idx_window = 1
        max_sum = 0
        for start in range(len(l1)):
            idx_window = start+1
            while idx_window <= len(l1)-1:
                curr_sum = sum(l1[start:idx_window])
                max_sum = max(max_sum, curr_sum)
                idx_window += 1
        print(max_sum)


# c1 = MaxSubSum()
# c1.findSum([-2, 1, -3, 4, -1, 2, 1, -5, 4])

# `Kadane's algorithm`
class Kalgo:
    def maxSum(self, l1):
        max_current = max_global = l1[0]
        for num in l1[1::]:
            max_current = max(num, max_current+num)
            max_global = max(max_current, max_global)
        return (max_global)


# c1 = Kalgo()
# c1.maxSum([-2, 1, -3, 4, -1, 2, 1, -5, 4])


class dMock:
    def vListing(self):
        wList = "Mon&Tues&Wed&Thurs"
        weeks = wList.split("&")
        print(weeks)
        print(weeks[3])
        print(weeks[3].upper())


# c1 = dMock()
# c1.vListing()

"""
- **Problem: Minimum Size Subarray Sum**
  - **Sample Input:** `[2,3,1,2,4,3]`, `7`
  - **Sample Output:** `2` (Explanation: The subarray [4,3] has a sum >= 7)

"""
