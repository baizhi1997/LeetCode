
# @Title: 数组的度 (Degree of an Array)
# @Author: qinxinlei
# @Date: 2018-11-06 15:52:36
# @Runtime: 72 ms
# @Memory: N/A

class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic=collections.defaultdict(int)
        l,r={},{}
        for i,num in enumerate(nums):
            dic[num]+=1
            if num not in l:
                l[num]=i
            r[num]=i
        tmp=max(dic.values())
        ans=math.inf
        for k,v in dic.items():
            if v==tmp:
                ans=min(ans,r[k]-l[k]+1)
        return ans
