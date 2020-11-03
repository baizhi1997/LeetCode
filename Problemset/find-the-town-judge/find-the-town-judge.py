
# @Title: 找到小镇的法官 (Find the Town Judge)
# @Author: qinxinlei
# @Date: 2019-02-28 15:32:27
# @Runtime: 100 ms
# @Memory: N/A

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        ans=[0]*(N+1)
        ans[0]=-1
        for t in trust:
            ans[t[0]]=-1
            ans[t[1]]+=1
        return ans.index(N-1) if N-1 in ans else -1
