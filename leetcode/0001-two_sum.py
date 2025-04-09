# Problem: Two Sum (LeetCode 1)
# Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Tags: Hash Map, Array
# Approach: Store each number's index in a dictionary, and check if complement exists.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
