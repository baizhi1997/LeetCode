
# @Title: 有效的字母异位词 (Valid Anagram)
# @Author: qinxinlei
# @Date: 2018-11-16 10:46:52
# @Runtime: 44 ms
# @Memory: N/A

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        cnt1=collections.Counter(s)
        cnt2=collections.Counter(t)
        return not (cnt1-cnt2) and not (cnt2-cnt1)
