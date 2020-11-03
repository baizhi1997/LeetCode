
# @Title: 连续数组 (Contiguous Array)
# @Author: qinxinlei
# @Date: 2018-12-03 20:50:13
# @Runtime: 192 ms
# @Memory: N/A

class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt=0
        dic={0:[-1,-1]}
        for i in range(len(nums)):
            if nums[i]:
                cnt+=1
            else:
                cnt-=1
            if cnt in dic:
                dic[cnt][1]=i
            else:
                dic[cnt]=[i,i]
        return max(v[1]-v[0] for v in dic.values())
