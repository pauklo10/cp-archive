# Problem: Palindrom Number (LeetCode 9)
# Link: https://leetcode.com/problems/palindrome-number/
# Difficulty: Easy
# Tags: Math
# Approach: Split number into sums of 10^n and divide to get individual digits, truncate and compare.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == 0:
            return True

        digits = []

        num_digits = math.floor(math.log10(x)) + 1
        mod = 10 ** num_digits
        power = mod // 10

        for _ in range(int(num_digits)):
            num = x % mod
            digit = num // power
            digits.append(digit)
            mod = mod // 10
            power = power // 10

        for i in range(len(digits) // 2):
            if digits[i] != digits[-1 - i]:
                return False

        return True
