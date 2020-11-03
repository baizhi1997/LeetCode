
# @Title: 制造字母异位词的最小步骤数 (Minimum Number of Steps to Make Two Strings Anagram)
# @Author: qinxinlei
# @Date: 2020-06-16 22:43:19
# @Runtime: 160 ms
# @Memory: 13.8 MB

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dic1 = collections.Counter(s)
        dic2 = collections.Counter(t)
        dic3 = dic1 - dic2
        return sum(dic3.values())
