
# @Title: 三角形的最大周长 (Largest Perimeter Triangle)
# @Author: qinxinlei
# @Date: 2019-03-01 16:01:20
# @Runtime: 72 ms
# @Memory: N/A

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        for i in range(len(A)-2):
            if A[i]<A[i+1]+A[i+2]:
                return A[i]+A[i+1]+A[i+2]
        return 0
