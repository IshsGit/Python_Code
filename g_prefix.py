
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
