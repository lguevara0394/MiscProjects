#solution for leetcode daily question
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = max(nums)
        max_length = curr_length = 0
        for i in nums:
            if (k < i):
                k = i
                max_length = curr_length = 0
            if (i==k):
                curr_length += 1
                max_length = max(max_length, curr_length)
            else:
                curr_length = 0
        return max_length