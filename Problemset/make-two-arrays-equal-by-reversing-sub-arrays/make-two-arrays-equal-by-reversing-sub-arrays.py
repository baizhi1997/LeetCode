
# @Title: 通过翻转子数组使两个数组相等 (Make Two Arrays Equal by Reversing Sub-arrays)
# @Author: qinxinlei
# @Date: 2020-07-28 16:12:35
# @Runtime: 36 ms
# @Memory: 13.3 MB

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        dic1 = collections.Counter(target)
        dic2 = collections.Counter(arr)
        return dic1 == dic2
