class Solution:
    def findDuplicates(nums):
        if len(nums) < 2:
            return []

        freq = {}
        for el in nums:
            if el not in freq:
                freq[el] = 1
            else:
                freq[el] += 1

        twice = []
        print(freq)
        for key in freq:
            if freq[key] == 2:
                twice.append(key)
        return twice


print(Solution.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
