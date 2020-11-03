
# @Title: 最长回文串 (Longest Palindrome)
# @Author: qinxinlei
# @Date: 2018-10-12 22:41:22
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic=collections.Counter(s)
        ans=0
        mark=0
        for c in dic:
            if dic[c]%2==0:
                ans+=dic[c]
            else:
                mark=1
                ans+=(dic[c]-1)
        return ans+mark
