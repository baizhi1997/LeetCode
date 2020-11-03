
# @Title: 分隔数组以得到最大和 (Partition Array for Maximum Sum)
# @Author: qinxinlei
# @Date: 2020-06-24 15:43:47
# @Runtime: 2916 ms
# @Memory: 13.3 MB

class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        dp = [0] * (len(A)+1)
        dp[0] = 0
        for i in range(len(A)):
            for j in range(K):
                if i-j>=0:
                    dp[i+1] = max(dp[i+1], dp[i-j] + max(A[i-j:i+1])*(j+1))
        print(dp)
        return dp[-1]
