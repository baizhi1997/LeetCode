
# @Title: 删除回文子序列 (Remove Palindromic Subsequences)
# @Author: qinxinlei
# @Date: 2020-08-02 11:19:07
# @Runtime: 40 ms
# @Memory: 13.3 MB

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        return 1 if s == s[::-1] else 2
