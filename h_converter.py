
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
