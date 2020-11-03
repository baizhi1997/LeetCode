
# @Title: 绝对值表达式的最大值 (Maximum of Absolute Value Expression)
# @Author: qinxinlei
# @Date: 2019-08-28 15:14:21
# @Runtime: 324 ms
# @Memory: N/A

class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        L1 = [arr1[i] - arr2[i] - i for i in range(len(arr1))]
        L2 = [arr1[i] + arr2[i] - i for i in range(len(arr1))]
        L3 = [arr1[i] + arr2[i] + i for i in range(len(arr1))]
        L4 = [arr1[i] - arr2[i] + i for i in range(len(arr1))]
        return max(max(L1) - min(L1), max(L2) - min(L2), max(L3) - min(L3), max(L4) - min(L4))
