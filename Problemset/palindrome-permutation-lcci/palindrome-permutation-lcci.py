
# @Title: 回文排列 (Palindrome Permutation LCCI)
# @Author: qinxinlei
# @Date: 2020-07-09 19:14:03
# @Runtime: 40 ms
# @Memory: 13.4 MB

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        dic = collections.Counter(s)
        cnt = 0
        for v in dic.values():
            if v & 1:
                cnt += 1
        return cnt < 2
