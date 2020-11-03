
# @Title: 复写零 (Duplicate Zeros)
# @Author: qinxinlei
# @Date: 2019-06-24 17:21:26
# @Runtime: 52 ms
# @Memory: N/A

class Solution:
    def duplicateZeros(self, A: List[int]) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        A[:] = [x for a in A for x in ([a] if a else [0, 0])][:len(A)]
