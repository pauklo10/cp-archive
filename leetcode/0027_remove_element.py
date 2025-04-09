# Problem: Two Sum (LeetCode 1)
# Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Tags: Hash Map, Array
# Approach: Move elements to back if num != val with counter, return counter.

class Solutions(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for num in nums:
            if num != val:
                nums[count] = num
                count += 1

        return count
