class Solution:

    def search(nums, target):
        if len(nums) == 1:
            if nums[0] != target:
                return False
            else:
                return True

        midpoint = int((len(nums)/2)//1)
        left = nums[:midpoint]
        right = nums[midpoint:]

        leftSearch = Solution.search(left, target)
        if leftSearch == False:
            rightSearch = Solution.search(right, target)
            if rightSearch != False:
                return True
            else:
                return rightSearch
        else:
            return leftSearch

    def searchMatrix(matrix, target):
        for arr in matrix:
            if Solution.search(arr, target) == True:
                return True

        return False


print(Solution.searchMatrix(
    [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 11))
