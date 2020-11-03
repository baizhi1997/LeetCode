
# @Title: 验证回文串 (Valid Palindrome)
# @Author: qinxinlei
# @Date: 2018-10-08 15:38:16
# @Runtime: 40 ms
# @Memory: N/A

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=''.join(c for c in s if c.isalnum()).lower()
        return s==s[::-1]
