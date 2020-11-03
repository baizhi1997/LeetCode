
# @Title: 最大连续1的个数 III (Max Consecutive Ones III)
# @Author: qinxinlei
# @Date: 2019-03-03 20:00:56
# @Runtime: 184 ms
# @Memory: N/A

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        j=0
        ans=0
        for i in range(len(A)):
            if A[i]==0 and K:
                K-=1
            elif A[i]==0:
                while A[j]!=0:
                    j+=1
                j+=1              
            ans=max(ans,i-j+1)
        return ans
