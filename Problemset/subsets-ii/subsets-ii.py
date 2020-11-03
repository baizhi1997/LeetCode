
# @Title: 子集 II (Subsets II)
# @Author: qinxinlei
# @Date: 2018-09-28 15:28:49
# @Runtime: 40 ms
# @Memory: N/A

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dic=collections.Counter(nums)
        ans=[[]]
        for num in dic:
            for i in range(len(ans)):
                for j in range(1,dic[num]+1):
                    ans.append(list(ans[i])+[num]*j)
        return ans

