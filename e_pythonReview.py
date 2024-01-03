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
