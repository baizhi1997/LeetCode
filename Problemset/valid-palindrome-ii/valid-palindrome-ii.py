
# @Title: 验证回文字符串 Ⅱ (Valid Palindrome II)
# @Author: qinxinlei
# @Date: 2018-10-08 15:54:28
# @Runtime: 88 ms
# @Memory: N/A

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return s[l:r]==s[l:r][::-1] or s[l+1:r+1]==s[l+1:r+1][::-1]
            l+=1
            r-=1         
        return True
