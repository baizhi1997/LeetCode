
# @Title: 行相等的最少多米诺旋转 (Minimum Domino Rotations For Equal Row)
# @Author: qinxinlei
# @Date: 2019-03-11 22:11:34
# @Runtime: 100 ms
# @Memory: N/A

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        for i in range(1, 7):
            if all(i == a or i == b for a, b in zip(A, B)):
                return  min(len(A) - A.count(i), len(B) - B.count(i))
        return -1
