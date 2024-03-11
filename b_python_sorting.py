class LongestConsecutiveSequence:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        nums = list(set(nums))  # Remove duplicates

        nums.sort()  # Sort the list

        longest_seq = 1
        current_seq = 1

        for i in range(1, len(nums)):
            # Check if the current element is consecutive to the previous one
            if nums[i] == nums[i - 1] + 1:
                current_seq += 1
            else:
                # If not consecutive, start a new sequence
                current_seq = 1

            # Update the longest sequence
            longest_seq = max(longest_seq, current_seq)

        return longest_seq


# Example usage:
# c1 = LongestConsecutiveSequence()
# result = c1.longestConsecutive([1, 3, 5, 7])
# print(result)

"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""


class MyMergeAgain:
    def isMerged(self, l1: list) -> list:
        sorted_list = sorted(l1)
        merged = [sorted_list[0]]
        for iv in sorted_list[1::]:
            # if curr<merged latest, then update
            if iv[0] < merged[-1][1]:
                merged[-1][1] = max(iv[1], merged[-1][1])
            else:
                merged.append(iv)
        print(merged)


# c1 = MyMergeAgain()
# c1.isMerged([[1, 3], [2, 6], [8, 10], [15, 18]])

"""
Problem 1: Find Gaps in Time Intervals
Given a list of time intervals representing
events throughout the day, find the gaps 
or free time between the intervals. 
Return a list of intervals representing 
the free time.
def find_free_time(intervals):
    # Your implementation here

# Example Usage:
intervals = [[1, 3], [2, 6], [8, 10], [9, 12], [14, 18]]
result = find_free_time(intervals)
print(result)
[[6, 8], [12, 14]]
"""
# if start point of interval is greater than
# end point of previous endpoint, then store
# those points into a list and append it to
# a gap list


class MyMergeFree:
    def find_free_time(self, intervals: list) -> list:
        sorted_intervals = sorted(intervals, key=lambda a: a[0])
        gap_list = []
        curr_int = sorted_intervals[0]
        for i in sorted_intervals[1::]:
            if i[0] > curr_int[1]:
                gap_list.append([curr_int[1], i[0]])
                curr_int = i
            else:
                curr_int[1] = max(curr_int[1], i[1])
        print(gap_list)


# c1 = MyMergeFree()
# c1.find_free_time([[1, 3], [2, 6], [8, 10], [9, 12], [14, 18]])
