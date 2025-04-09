# Problem: Merge Sorted Array (LeetCode 88)
# Link: https://leetcode.com/problems/merge-sorted-array/
# Difficulty: Easy
# Tags: Array, Two Pointers, Sorting
# Approach: Iterate both lists backwards and reassign values. Adjoin leftover values of num2 if any.

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        insert = m + n - 1
        while j >= 0 and i >= 0:
            if nums1[i] <= nums2[j]: 
                nums1[insert] = nums2[j]
                j -= 1
            else:
                nums1[insert] = nums1[i]
                i -= 1
            insert -= 1
        
        for x in range(j+1):
            nums1[x] = nums2[x]
