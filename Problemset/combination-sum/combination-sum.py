
# @Title: 组合总和 (Combination Sum)
# @Author: qinxinlei
# @Date: 2018-09-23 11:34:59
# @Runtime: 44 ms
# @Memory: N/A

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dp={0:[[]]}
        candidates.sort()
        def f(target):
            ans=[]
            for k in candidates:
                if k>target:
                    break
                if target-k not in dp:
                    f(target-k)
                for d in dp[target-k]:
                    if len(d)==0 or d[-1]<=k:
                        ans.append(d+[k])             
            dp[target]=ans   
            
        f(target)
        return dp[target]

