
"""
Technique: Prefix Sum
Description: The PrefixSum class computes the prefix sum of the
input array. The range_sum method then calculates the sum of 
elements in a given range using the prefix sum array.
"""
# Example Usage:
# nums = [1, 2, 3, 4, 5]
# prefix_sum = PrefixSum(nums)
# result = prefix_sum.range_sum(1, 3)
# print(result)  # Expected Output: Sum of elements from index 1 to 3

"""
 Running Maximum
Technique: Prefix Maximum
Description: The PrefixMax class computes the prefix 
maximum of the input array. The range_max method then 
retrieves the maximum element in a given range using 
the prefix maximum array.
"""


class PrefixMax:
    def __init__(self, nums):
        # Initialize prefix maximum array
        self.nums = nums

    def range_max(self, left, right):
        # Find and return the maximum element in the range [left, right]
        curr_max = self.nums[left]
        max_element = self.nums[left]
        for x in range(left+1, right+1):
            max_element = max(max_element, self.nums[x])
        return max_element


# Example Usage:
# nums = [3, 1, 5, 2, 7]
# prefix_max = PrefixMax(nums)
# result = prefix_max.range_max(1, 3)

# print(result)  # Expected Output: 5
"""
Problem:
Given an array of integers, precompute the prefix count array. 
Implement a function to efficiently count the occurrences of
a specific value in a given range.
Counting Occurrences
Technique: Prefix Count
Description: The PrefixCount class computes the prefix count 
of a specific value (e.g., 2) in the input array. The 
count_occurrences method then calculates the number of 
occurrences of the value in a given range using the 
prefix count array.
"""


class PrefixCount:
    def __init__(self, nums):
        # Initialize prefix count array
        self.nums = nums

    def count_occurrences(self, value, left, right):
        # Count and return the occurrences of 'value' in the range [left, right]
        count = 0
        target = value
        for x in range(left, right+1):
            if self.nums[x] == target:
                count += 1
        return count


# Example Usage:note
# nums = [2, 5, 2, 8, 2, 3, 1, 2]
# prefix_count = PrefixCount(nums)
# result = prefix_count.count_occurrences(2, 2, 6)
# print(result)  # Expected Output: 3
