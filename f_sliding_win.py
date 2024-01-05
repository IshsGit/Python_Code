# Technique/Algorithm: Sliding Window
# Example:
# s = "abcabcbb"
# print(lengthOfLongestSubstring(s))
# Output: 3

class MyProduct:
    def productExceptSelf(nums):
        # Initialize two arrays, left_products and right_products
        # Compute the product of all elements to the left of each element and store in left_products
        # Compute the product of all elements to the right of each element and store in right_products
        # Multiply corresponding elements from left_products and right_products to get the final result
        n = len(nums)
        left_product = [1]*n
        right_product = [1]*n
        result = []
        # left_product =[1,1,2,6]
        # right_product=[24,12,4,1]
        for i in range(1, n):
            left_product[i] = left_product[i-1]*nums[i-1]
        for i in range(n-2, -1, -1):
            right_product[i] = right_product[i+1]*nums[i+1]

        for idx, x in enumerate(nums):
            result.append(left_product[idx]*right_product[idx])
        return result
# Technique/Algorithm: Prefix Product Arrays
# Example:
# nums = [1, 2, 3, 4]
# print(MyProduct.productExceptSelf(nums))
# Output: [24, 12, 8, 6]


"""
 Sum of Elements in a Range
Problem: Given an array of integers, precompute the prefix sum 
array. Implement a function to efficiently calculate the sum 
of elements in a given range.
"""


class PrefixSum:
    def __init__(self, nums):
        # Initialize prefix sum array
        self.nums = nums

    def range_sum(self, left, right):
        # Calculate and return the sum of elements in the range [left, right]
        prefix_sum = self.nums[left]
        for x in range(left+1, right+1):
            prefix_sum = prefix_sum+self.nums[x]
        return prefix_sum
