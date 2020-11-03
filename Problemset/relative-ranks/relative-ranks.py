
# @Title: 相对名次 (Relative Ranks)
# @Author: qinxinlei
# @Date: 2018-11-01 15:56:41
# @Runtime: 56 ms
# @Memory: N/A

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        s=sorted(nums,reverse=True)
        dic=collections.defaultdict()
        for i in range(len(nums)):
            dic[s[i]]=i+1
        ans=[]
        for num in nums:
            tmp=dic[num]
            if tmp<4:
                if tmp==1:
                    ans.append("Gold Medal")
                elif tmp==2:
                    ans.append("Silver Medal")
                else:
                    ans.append("Bronze Medal")
            else:
                ans.append(str(tmp))
        return ans
