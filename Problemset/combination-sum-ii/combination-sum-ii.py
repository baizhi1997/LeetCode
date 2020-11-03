
# @Title: 组合总和 II (Combination Sum II)
# @Author: qinxinlei
# @Date: 2018-09-28 10:27:54
# @Runtime: 40 ms
# @Memory: N/A

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results=[]
        candidates.sort()
        def f(nums,target,result):
            for i in range (len(nums)):
                if i and nums[i]==nums[i-1]:
                    continue
                if nums[i]==target:
                    results.append(result+[nums[i]])
                    break
                elif target<nums[i]:
                    break
                else:
                    f(nums[i+1:],target-nums[i],result+[nums[i]])                
        f(candidates,target,[])
        return results
