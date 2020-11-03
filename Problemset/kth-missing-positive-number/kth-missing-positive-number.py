
# @Title: 第 k 个缺失的正整数 (Kth Missing Positive Number)
# @Author: qinxinlei
# @Date: 2020-08-12 18:03:04
# @Runtime: 52 ms
# @Memory: 13 MB

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        pre = 0
        for i in range(len(arr)):
            k -= (arr[i]-pre-1)
            pre = arr[i]
            if k <= 0:
                return arr[i]+k-1
        return arr[-1]+k
