
# @Title: 判定是否互为字符重排 (Check Permutation LCCI)
# @Author: qinxinlei
# @Date: 2020-07-08 22:54:46
# @Runtime: 32 ms
# @Memory: 13.3 MB

class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return sorted(s1) == sorted(s2)
