
# @Title: K 次取反后最大化的数组和 (Maximize Sum Of Array After K Negations)
# @Author: qinxinlei
# @Date: 2019-03-11 21:11:26
# @Runtime: 40 ms
# @Memory: N/A

class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        i = 0
        while i < len(A) and i < K and A[i] < 0:
            A[i] = -A[i]
            i += 1
        return sum(A) - (K - i) % 2 * min(A) * 2
