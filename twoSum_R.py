# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


# turn array into hash where index is key and value is element
# check if diff exist in the array hash

class twoSum:
    def Solution(arr, target):
        arrMap = {}
        for idx, num in enumerate(arr):
            if target-num in arrMap:
                return [arrMap[target-num], idx]
            arrMap[num] = idx
        return []


# print(twoSum.Solution([1, 5, 2, 6, 3, 7, 8], 9))

class biggestDiff:
    def solution(arr):
        smallest = arr[0]
        largest = arr[0]
        for num in arr:
            if num < smallest:
                smallest = num
            if num > largest:
                largest = num
        return largest-smallest


# print(biggestDiff.solution([4, 1, 2]))


# Finding Duplicates
# Problem: Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.

class findingDuplciates:
    def solution(nums):
        numsMap = {}
        for idx, num in enumerate(nums):
            if num in numsMap:
                return True
            else:
                numsMap[num] = 1

        return False


# Example 1
# nums = [1, 2, 3, 1]
# print(findingDuplciates.solution(nums))

# 3. Frequency Counting
# Problem: Given a string s, find the first non-repeating character in it
# and return its index. If it does not exist, return -1.

class Frequency:
    def solution(s):
        freq = {}
        for idx, ch in enumerate(s):
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch] += 1

        for idx, ch in enumerate(s):
            if freq[ch] == 1:
                return idx


d
return -1


# Example 2
# s = "loveleetcode"
# print(Frequency.solution(s))
# Output: 2

# Anagram Checking
# Problem: Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1
s = "anagram"
t = "nagaram"
# Output: true

# # Example 2
# s = "rat"
# t = "car"
# # Output: false

# # Example 3
# s = "listen"
# t = "silent"
# Output: true
