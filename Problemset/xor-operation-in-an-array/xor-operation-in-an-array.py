
# @Title: 数组异或操作 (XOR Operation in an Array)
# @Author: qinxinlei
# @Date: 2020-07-28 12:16:19
# @Runtime: 44 ms
# @Memory: 13.2 MB

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        for i in range(n):
            ans ^= start
            start += 2
        return ans
