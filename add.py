# def longestsubstring(s: str) -> int:
#     idx_map = {}
#     max_length = 0
#     start = 0

#     for end in range(len(s)):
#         if s[end] in idx_map:
#             start = max(start, idx_map[s[end]]+1)
#         idx_map[s[end]] = end
#         max_length = max(max_length, end-start+1)

#     return max_length


# def usinghash(s: str):
#     idx_map = {}
#     for idx in idx_map:
#         idx_map[idx] = idx_map.get(idx, 0)
#     print(idx_map)

# nums = [1, 2, 3]
# print(nums[:])

class Solution:
    def permute(nums):
        # base step
        if len(nums) <= 1:
            return nums
        perm = [nums]

        # recursive step

        # [1,2,3]
        # [2,1,3]
        # [2,3,1]
        # [1,3,2]
        # [3,2,1]

        # iterative step
        for i, num in enumerate(nums):
            if i < len(nums)-1:
                j = i+1
            else:
                j = 0
            while j != i:
                subarr = nums[:]
                print("i", i)
                print("j", j)
                subarr[i], subarr[j] = subarr[j], subarr[i]
                if subarr not in perm:
                    perm.append(subarr)
                print("perm:", perm)
                if j == len(nums)-1:
                    j = 0
                else:
                    j += 1
        print("final perm: ", perm)


Solution.permute([1, 2, 3])

# [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
