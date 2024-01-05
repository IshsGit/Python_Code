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
