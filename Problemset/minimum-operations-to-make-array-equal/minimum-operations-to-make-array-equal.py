
# @Title: 使数组中所有元素相等的最小操作数 (Minimum Operations to Make Array Equal)
# @Author: qinxinlei
# @Date: 2020-08-17 15:54:28
# @Runtime: 120 ms
# @Memory: 13.4 MB

class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0
        for i in range(n//2):
            ans += (n-1-i*2)
        return ans
